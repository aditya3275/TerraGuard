from app.models import (
    CriticalityReport,
    ResourceRisk,
    ResourceRiskReport,
    SecurityReport,
)


class ResourceCorrelator:
    """
    Correlates graph criticality with
    security findings.
    """

    def correlate(
        self,
        criticality_report: CriticalityReport,
        security_report: SecurityReport,
    ) -> ResourceRiskReport:

        resources = []

        for item in criticality_report.resources:

            findings = [
                finding
                for finding in security_report.findings
                if finding.resource == item.resource
            ]

            resources.append(
                ResourceRisk(
                    criticality=item,
                    findings=findings,
                )
            )

        return ResourceRiskReport(resources=resources)
