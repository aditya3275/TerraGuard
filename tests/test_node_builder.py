import json

from app.graph.node_builder import NodeBuilder
from app.parser.terraform_parser import TerraformParser


def test_node_builder():

    with open(
        "terraform_examples/basic_vpc/plan.json",
        "r",
    ) as file:
        terraform_json = json.load(file)

    blueprint = TerraformParser().build_blueprint(terraform_json)

    nodes = NodeBuilder().build_nodes(blueprint)

    assert len(nodes) == 4

    assert "aws_vpc.main" in nodes

    assert "aws_subnet.public" in nodes

    assert "aws_security_group.web_sg" in nodes

    assert "aws_instance.web" in nodes
