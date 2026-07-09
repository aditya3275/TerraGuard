import json

from app.graph.infrastructure_graph_builder import (
    InfrastructureGraphBuilder,
)
from app.graph.services.graph_service import (
    GraphService,
)
from app.parser.terraform_parser import (
    TerraformParser,
)


def test_blast_radius():

    with open(
        "terraform_examples/basic_vpc/plan.json",
        "r",
    ) as file:
        terraform_json = json.load(file)

    blueprint = TerraformParser().build_blueprint(terraform_json)

    graph = InfrastructureGraphBuilder().build_graph(blueprint)

    affected = GraphService().blast_radius_analysis(
        graph,
        "aws_vpc.main",
    )

    assert set(affected) == {
        "aws_vpc.main",
        "aws_subnet.public",
        "aws_security_group.web_sg",
        "aws_instance.web",
    }
