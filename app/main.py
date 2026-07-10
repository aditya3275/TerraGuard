from app.engine.terraguard_engine import (
    TerraGuardEngine,
)

from app.github.markdown import (
    GitHubMarkdownRenderer,
)


def main():

    report = TerraGuardEngine().analyze(
        terraform_directory="terraform_examples/basic_vpc",
        plan_json_path="terraform_examples/basic_vpc/plan.json",
    )

    markdown = GitHubMarkdownRenderer().render(report)

    with open(
        "report.md",
        "w",
        encoding="utf-8",
    ) as file:

        file.write(markdown)

    print()

    print("GitHub report generated successfully.")

    print("Output file : report.md")


if __name__ == "__main__":
    main()
