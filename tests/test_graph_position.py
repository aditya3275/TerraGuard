import json

from app.graph.algorithms.graph_position import (
    GraphPositionAnalyzer,
)
from app.graph.infrastructure_graph_builder import (
    InfrastructureGraphBuilder,
)
from app.models import GraphPosition
from app.parser.terraform_parser import (
    TerraformParser,
)


def test_graph_position():

    with open("terraform_examples/basic_vpc/plan.json") as file:
        terraform_json = json.load(file)

    blueprint = TerraformParser().build_blueprint(terraform_json)

    graph = InfrastructureGraphBuilder().build_graph(blueprint)

    analyzer = GraphPositionAnalyzer()

    assert (
        analyzer.analyze(
            graph,
            "aws_vpc.main",
        )
        == GraphPosition.ROOT
    )

    assert (
        analyzer.analyze(
            graph,
            "aws_subnet.public",
        )
        == GraphPosition.INTERMEDIATE
    )

    assert (
        analyzer.analyze(
            graph,
            "aws_instance.web",
        )
        == GraphPosition.LEAF
    )
