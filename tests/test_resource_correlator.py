from app.correlation.resource_correlator import (
    ResourceCorrelator,
)

from app.models import (
    CriticalityItem,
    CriticalityLevel,
    CriticalityReport,
    SecurityFinding,
    SecurityReport,
)


def test_resource_correlator():

    criticality = CriticalityReport(
        resources=[
            CriticalityItem(
                resource="aws_security_group.web_sg",
                score=65,
                level=CriticalityLevel.MEDIUM,
                dependency_count=1,
                blast_radius=2,
                rank=1,
            )
        ]
    )

    security = SecurityReport(
        findings=[
            SecurityFinding(
                check_id="CKV_AWS_24",
                title="SSH open to the Internet",
                severity="UNKNOWN",
                resource="aws_security_group.web_sg",
            )
        ]
    )

    report = ResourceCorrelator().correlate(
        criticality,
        security,
    )

    resource = report.resources[0]

    assert resource.has_findings()

    assert resource.total_findings() == 1

    assert resource.check_ids() == ["CKV_AWS_24"]
