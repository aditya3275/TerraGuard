from pydantic import BaseModel, Field

from app.models.resource_risk import ResourceRisk


class ResourceRiskReport(BaseModel):
    """
    Correlated infrastructure risk report.
    """

    resources: list[ResourceRisk] = Field(default_factory=list)
