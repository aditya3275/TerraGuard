from pydantic import BaseModel

from .decision_report import DecisionReport
from .resource_risk_report import ResourceRiskReport


class AnalysisReport(BaseModel):
    """
    Final report produced by TerraGuard.

    Exposes only the information that
    consumers of TerraGuard need.
    """

    risk_report: ResourceRiskReport

    decision: DecisionReport
