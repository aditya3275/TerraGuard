from pydantic import BaseModel, Field

from .security_finding import SecurityFinding


class SecurityReport(BaseModel):
    """
    Collection of security findings.
    """

    analyzer: str = "checkov"

    findings: list[SecurityFinding] = Field(default_factory=list)

    def total_findings(self) -> int:
        return len(self.findings)
