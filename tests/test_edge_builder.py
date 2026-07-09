import json

from app.graph.edge_builder import EdgeBuilder
from app.parser.terraform_parser import TerraformParser


def test_edge_builder():

    with open(
        "terraform_examples/basic_vpc/plan.json",
        "r",
    ) as file:

        terraform_json = json.load(file)

    blueprint = TerraformParser().build_blueprint(terraform_json)

    edges = EdgeBuilder().build_edges(blueprint)

    assert len(edges) == 4

    edge_pairs = {(edge.source, edge.target) for edge in edges}

    assert (
        "aws_instance.web",
        "aws_subnet.public",
    ) in edge_pairs

    assert (
        "aws_instance.web",
        "aws_security_group.web_sg",
    ) in edge_pairs

    assert (
        "aws_subnet.public",
        "aws_vpc.main",
    ) in edge_pairs

    assert (
        "aws_security_group.web_sg",
        "aws_vpc.main",
    ) in edge_pairs
