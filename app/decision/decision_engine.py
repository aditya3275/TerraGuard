from app.models import (
    CriticalityLevel,
    DecisionReport,
    DecisionSummary,
    ResourceRiskReport,
)


class DecisionEngine:
    """
    Produces the final deployment recommendation
    based on correlated infrastructure risk.
    """

    def evaluate(
        self,
        report: ResourceRiskReport,
    ) -> DecisionReport:

        reasons = []
        recommendations = []

        total_findings = sum(resource.total_findings() for resource in report.resources)

        # Rule 1
        if total_findings == 0:

            reasons.append("No unresolved security findings were detected.")

            recommendations.append("Infrastructure is ready for deployment.")

            return DecisionReport(
                decision=DecisionSummary.APPROVE,
                reasons=reasons,
                recommendations=recommendations,
            )

        # Rule 2
        for resource in report.resources:

            if (
                resource.criticality.level
                in (
                    CriticalityLevel.CRITICAL,
                    CriticalityLevel.HIGH,
                )
                and resource.has_findings()
            ):

                reasons.append(
                    (
                        f"{resource.criticality.resource} "
                        "is operationally important "
                        "and contains unresolved "
                        "security findings."
                    )
                )

                recommendations.append(
                    (
                        f"Review and resolve security findings for "
                        f"{resource.criticality.resource}."
                    )
                )

                recommendations.append("Re-run TerraGuard before merging.")

                return DecisionReport(
                    decision=DecisionSummary.BLOCK,
                    reasons=reasons,
                    recommendations=recommendations,
                )

        # Rule 3

        reasons.append(
            (
                "Security findings exist, but none affect "
                "high-criticality infrastructure."
            )
        )

        recommendations.append("Review security findings before deployment.")

        recommendations.append("Monitor affected resources after deployment.")

        return DecisionReport(
            decision=DecisionSummary.WARN,
            reasons=reasons,
            recommendations=recommendations,
        )
