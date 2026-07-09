from app.models import (
    CriticalityItem,
    CriticalityLevel,
    ResourceRisk,
    ResourceRiskReport,
    SecurityFinding,
)
from app.renderers.resource_risk_renderer import (
    ResourceRiskRenderer,
)


def test_resource_risk_renderer():

    report = ResourceRiskReport(
        resources=[
            ResourceRisk(
                criticality=CriticalityItem(
                    resource="aws_security_group.web_sg",
                    score=65,
                    level=CriticalityLevel.MEDIUM,
                    dependency_count=3,
                    blast_radius=3,
                    rank=1,
                ),
                findings=[
                    SecurityFinding(
                        check_id="CKV_AWS_24",
                        title="Ensure no security groups allow SSH from 0.0.0.0/0",
                        severity="UNKNOWN",
                        resource="aws_security_group.web_sg",
                    )
                ],
            )
        ]
    )

    output = ResourceRiskRenderer().render(report)

    assert "Resource Risk" in output
    assert "Insights" in output
    assert "aws_security_group.web_sg" in output
    assert "CKV_AWS_24" in output
