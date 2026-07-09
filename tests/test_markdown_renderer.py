from app.models import (
    CriticalityItem,
    CriticalityLevel,
    CriticalityReport,
)
from app.renderers.markdown_renderer import (
    MarkdownRenderer,
)


def test_markdown_renderer():

    report = CriticalityReport(
        resources=[
            CriticalityItem(
                resource="aws_vpc.main",
                score=97,
                level=CriticalityLevel.CRITICAL,
                dependency_count=3,
                blast_radius=4,
                rank=1,
            )
        ]
    )

    markdown = MarkdownRenderer().render(report)

    assert "Infrastructure Criticality Report" in markdown

    assert "aws_vpc.main" in markdown

    assert "97" in markdown
