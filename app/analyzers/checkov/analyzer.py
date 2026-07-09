import json
import subprocess


class CheckovAnalyzer:
    """
    Executes Checkov against a Terraform directory.
    """

    def analyze(
        self,
        terraform_directory: str,
    ) -> dict:

        result = subprocess.run(
            [
                "checkov",
                "-d",
                terraform_directory,
                "-o",
                "json",
            ],
            capture_output=True,
            text=True,
        )

        # A non-zero exit code is expected when
        # Checkov finds policy violations.
        if not result.stdout.strip():
            raise RuntimeError(f"Checkov failed:\n{result.stderr}")

        return json.loads(result.stdout)
