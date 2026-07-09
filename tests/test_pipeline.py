import json

from app.pipeline.pipeline import (
    TerraGuardPipeline,
)


def test_pipeline():

    with open("terraform_examples/basic_vpc/plan.json") as file:

        terraform_json = json.load(file)

    output = TerraGuardPipeline().run(terraform_json)

    assert "Infrastructure Criticality Report" in output

    assert "aws_vpc.main" in output
