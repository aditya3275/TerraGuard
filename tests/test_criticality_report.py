from app.models import (
    CriticalityItem,
    CriticalityLevel,
    CriticalityReport,
)


def test_criticality_report():

    report = CriticalityReport(
        resources=[
            CriticalityItem(
                resource="vpc",
                score=97,
                level=CriticalityLevel.CRITICAL,
                dependency_count=5,
                blast_radius=6,
                rank=1,
            ),
            CriticalityItem(
                resource="subnet",
                score=81,
                level=CriticalityLevel.HIGH,
                dependency_count=3,
                blast_radius=4,
                rank=2,
            ),
        ]
    )

    assert report.total_resources() == 2

    assert report.highest_risk().resource == "vpc"

    assert len(report.top_resources(1)) == 1

    summary = report.summary()

    assert summary[CriticalityLevel.CRITICAL] == 1

    assert summary[CriticalityLevel.HIGH] == 1

    grouped = report.grouped_resources()

    assert grouped[CriticalityLevel.CRITICAL][0].resource == "vpc"
