from pydantic import BaseModel, Field

from .decision_summary import DecisionSummary


class DecisionReport(BaseModel):
    """
    Final deployment recommendation
    produced by TerraGuard.
    """

    decision: DecisionSummary

    reasons: list[str] = Field(
        default_factory=list,
    )

    recommendations: list[str] = Field(
        default_factory=list,
    )
