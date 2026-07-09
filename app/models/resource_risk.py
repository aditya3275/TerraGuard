from pydantic import BaseModel

from app.knowledge.infrastructure import (
    RESOURCE_INSIGHTS,
)

from app.models import (
    CriticalityItem,
    SecurityFinding,
)


class ResourceRisk(BaseModel):
    """
    Represents the complete risk profile
    of a single infrastructure resource.
    """

    criticality: CriticalityItem

    findings: list[SecurityFinding]

    def total_findings(self) -> int:
        return len(self.findings)

    def has_findings(self) -> bool:
        return self.total_findings() > 0

    def check_ids(self) -> list[str]:
        return [finding.check_id for finding in self.findings]

    def risk_level(self) -> str:
        """
        TerraGuard's deterministic
        resource risk assessment.
        """

        score = self.criticality.score
        findings = self.total_findings()

        if score >= 90 and findings > 0:
            return "Critical"

        if score >= 70 and findings > 0:
            return "High"

        if score >= 50 and findings > 0:
            return "Medium"

        if findings >= 3:
            return "Medium"

        if findings > 0:
            return "Low"

        return "Low"

    def insights(self) -> list[str]:
        """
        Generates operational insights
        for this resource.
        """

        insights = []

        score = self.criticality.score
        blast_radius = self.criticality.blast_radius
        findings = self.total_findings()

        # Infrastructure Insight
        resource_type = self.criticality.resource.split(".")[0]

        description = RESOURCE_INSIGHTS.get(resource_type)

        if description:
            insights.append(description)

        # Security Insight
        if findings >= 3:
            insights.append(
                "Multiple failed security checks indicate increased operational exposure."
            )

        elif findings > 0:
            insights.append(
                "Security policy violations should be reviewed before deployment."
            )

        # Dependency Insight
        if blast_radius >= 10:
            insights.append(
                "Changes could impact a large portion of the infrastructure."
            )

        elif blast_radius >= 3:
            insights.append("Changes may affect dependent infrastructure resources.")

        # Combined Operational Insight
        if score >= 70 and findings > 0:
            insights.append(
                "This resource combines high operational importance with unresolved security findings."
            )

        return insights
