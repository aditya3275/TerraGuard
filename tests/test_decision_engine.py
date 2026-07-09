from app.decision.decision_engine import (
    DecisionEngine,
)

from app.models import (
    CriticalityItem,
    CriticalityLevel,
    CriticalityReport,
    DecisionSummary,
    ResourceRisk,
    ResourceRiskReport,
    SecurityFinding,
    decision,
)


def test_block_decision():

    report = ResourceRiskReport(
        resources=[
            ResourceRisk(
                criticality=CriticalityItem(
                    resource="aws_vpc.main",
                    score=97,
                    level=CriticalityLevel.CRITICAL,
                    dependency_count=3,
                    blast_radius=10,
                    rank=1,
                ),
                findings=[
                    SecurityFinding(
                        check_id="CKV_AWS_23",
                        title="Example",
                        severity="UNKNOWN",
                        resource="aws_vpc.main",
                    )
                ],
            )
        ]
    )

    decision = DecisionEngine().evaluate(report)

    assert decision.decision == DecisionSummary.BLOCK

    assert len(decision.reasons) == 1

    assert len(decision.recommendations) == 2
