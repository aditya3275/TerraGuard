from app.engine.terraguard_engine import (
    TerraGuardEngine,
)
from app.renderers.resource_risk_renderer import (
    ResourceRiskRenderer,
)


def main():

    report = TerraGuardEngine().analyze(
        terraform_directory="terraform_examples/basic_vpc",
        plan_json_path="terraform_examples/basic_vpc/plan.json",
    )

    print()

    print(ResourceRiskRenderer().render(report.risk_report))

    print()

    print("Decision")
    print("--------")

    print(report.decision.decision.value)

    print()

    print("Reasons")
    print("-------")

    for reason in report.decision.reasons:
        print(f"• {reason}")

    print()

    print("Recommendations")
    print("---------------")

    for recommendation in report.decision.recommendations:
        print(f"• {recommendation}")


if __name__ == "__main__":
    main()
