from app.models import (
    SecurityFinding,
    SecurityReport,
)


class CheckovParser:
    """
    Converts raw Checkov JSON into a SecurityReport.
    """

    def parse(
        self,
        checkov_json: list,
    ) -> SecurityReport:

        findings = []

        if not checkov_json:
            return SecurityReport(findings=[])

        results = checkov_json[0].get(
            "results",
            {},
        )

        failed_checks = results.get(
            "failed_checks",
            [],
        )

        for check in failed_checks:

            findings.append(
                SecurityFinding(
                    check_id=check.get(
                        "check_id",
                        "",
                    ),
                    title=check.get(
                        "check_name",
                        "",
                    ),
                    severity=(check.get("severity") or "UNKNOWN"),
                    resource=check.get(
                        "resource",
                        "",
                    ),
                    file_path=check.get(
                        "file_path",
                    ),
                    guideline=check.get(
                        "guideline",
                    ),
                )
            )

        return SecurityReport(
            findings=findings,
        )
