import json

from app.graph.infrastructure_graph_builder import (
    InfrastructureGraphBuilder,
)

from app.parser.terraform_parser import TerraformParser


def test_graph_builder_creates_nodes():

    with open(
        "terraform_examples/basic_vpc/plan.json",
        "r",
    ) as file:
        terraform_json = json.load(file)

    blueprint = TerraformParser().build_blueprint(terraform_json)

    graph = InfrastructureGraphBuilder().build_graph(blueprint)

    assert len(graph.nodes) == 4

    assert "aws_vpc.main" in graph.nodes

    assert "aws_subnet.public" in graph.nodes

    assert "aws_security_group.web_sg" in graph.nodes

    assert "aws_instance.web" in graph.nodes
