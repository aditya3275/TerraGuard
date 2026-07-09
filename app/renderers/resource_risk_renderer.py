from app.models import (
    ResourceRiskReport,
)


class ResourceRiskRenderer:
    """
    Renders the correlated TerraGuard
    resource risk report.
    """

    def render(
        self,
        report: ResourceRiskReport,
    ) -> str:

        lines = []

        lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        lines.append("🛡 TerraGuard Resource Risk Report")
        lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        lines.append("")

        for resource in report.resources:

            criticality = resource.criticality

            lines.append("Resource")
            lines.append("--------")
            lines.append(criticality.resource)
            lines.append("")

            lines.append("Infrastructure")
            lines.append("--------------")
            lines.append(f"Criticality Score : {criticality.score}")
            lines.append(f"Graph Level       : {criticality.level.value}")
            lines.append(f"Blast Radius      : {criticality.blast_radius}")
            lines.append("")

            lines.append("Security")
            lines.append("--------")
            lines.append(f"Failed Checks : {resource.total_findings()}")

            if resource.has_findings():

                lines.append("")
                lines.append("Checks")
                lines.append("------")

                for finding in resource.findings:

                    lines.append(f"• {finding.check_id}")

                    lines.append(f"  {finding.title}")

            lines.append("")

            lines.append("Resource Risk")
            lines.append("-------------")
            lines.append(resource.risk_level())
            lines.append("")

            lines.append("Insights")
            lines.append("--------")

            for insight in resource.insights():
                lines.append(f"• {insight}")

            lines.append("")
            lines.append("══════════════════════════════════════════════════")
            lines.append("")

        return "\n".join(lines)
