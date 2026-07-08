import json

from app.parser.terraform_parser import TerraformParser


def test_build_blueprint():
    with open(
        "terraform_examples/basic_vpc/plan.json",
        "r",
    ) as file:
        terraform_json = json.load(file)

    parser = TerraformParser()

    blueprint = parser.build_blueprint(terraform_json)

    assert blueprint.metadata.terraform_version.startswith("1.")
    assert len(blueprint.resource_changes) == 4
