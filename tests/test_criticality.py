import json

from app.graph.algorithms.criticality import (
    CriticalityAnalyzer,
)
from app.graph.infrastructure_graph_builder import (
    InfrastructureGraphBuilder,
)
from app.parser.terraform_parser import (
    TerraformParser,
)


def test_criticality():

    with open("terraform_examples/basic_vpc/plan.json") as file:
        terraform_json = json.load(file)

    blueprint = TerraformParser().build_blueprint(terraform_json)

    graph = InfrastructureGraphBuilder().build_graph(blueprint)

    report = CriticalityAnalyzer().analyze(graph)

    assert len(report.resources) == 4

    assert report.resources[0].resource == "aws_vpc.main"

    assert report.resources[-1].resource == "aws_instance.web"
