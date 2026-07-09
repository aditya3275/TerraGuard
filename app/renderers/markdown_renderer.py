from app.models import (
    CriticalityLevel,
    CriticalityReport,
)


class MarkdownRenderer:
    """
    Renders a CriticalityReport as Markdown.
    """

    LEVEL_HEADERS = {
        CriticalityLevel.CRITICAL: "🟥 Critical (90–100)",
        CriticalityLevel.HIGH: "🟧 High (70–89)",
        CriticalityLevel.MEDIUM: "🟨 Medium (50–69)",
        CriticalityLevel.LOW: "🟩 Low (<50)",
    }

    def render(
        self,
        report: CriticalityReport,
    ) -> str:

        lines = []

        lines.append("# 📊 Infrastructure Criticality Report")
        lines.append("")

        summary = report.summary()

        lines.append("## Summary")
        lines.append("")
        lines.append(f"- Critical : {summary[CriticalityLevel.CRITICAL]}")
        lines.append(f"- High     : {summary[CriticalityLevel.HIGH]}")
        lines.append(f"- Medium   : {summary[CriticalityLevel.MEDIUM]}")
        lines.append(f"- Low      : {summary[CriticalityLevel.LOW]}")
        lines.append("")

        for level, resources in report.grouped_resources().items():

            if not resources:
                continue

            lines.append(f"## {self.LEVEL_HEADERS[level]}")
            lines.append("")

            for item in resources:

                lines.append(f"### [{item.rank}] {item.resource}")
                lines.append(f"- Score: **{item.score}**")
                lines.append(f"- Dependents: {item.dependency_count}")
                lines.append(f"- Blast Radius: {item.blast_radius}")
                lines.append("")

        return "\n".join(lines)
