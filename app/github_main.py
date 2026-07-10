from app.engine.terraguard_engine import (
    TerraGuardEngine,
)

from app.github.reporter import (
    GitHubReporter,
)


def main():

    report = TerraGuardEngine().analyze(
        terraform_directory="terraform_examples/basic_vpc",
        plan_json_path="terraform_examples/basic_vpc/plan.json",
    )

    GitHubReporter().publish(
        report=report,
        owner="aditya3275",
        repository="TerraGuard",
        pull_request=1,
    )

    print()

    print("TerraGuard GitHub report published successfully.")


if __name__ == "__main__":
    main()
