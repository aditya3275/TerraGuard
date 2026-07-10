import os

from app.engine.terraguard_engine import (
    TerraGuardEngine,
)

from app.github.reporter import (
    GitHubReporter,
)


def main():

    owner = os.environ["GITHUB_OWNER"]

    repository = os.environ["GITHUB_REPOSITORY_NAME"]

    pull_request = int(os.environ["GITHUB_PR_NUMBER"])

    report = TerraGuardEngine().analyze(
        terraform_directory="terraform_examples/basic_vpc",
        plan_json_path="terraform_examples/basic_vpc/plan.json",
    )

    GitHubReporter().publish(
        report=report,
        owner=owner,
        repository=repository,
        pull_request=pull_request,
    )

    print()

    print("TerraGuard GitHub Action completed successfully.")


if __name__ == "__main__":
    main()
