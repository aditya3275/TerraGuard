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


def test_dependency_count():

    with open(
        "terraform_examples/basic_vpc/plan.json",
        "r",
    ) as file:

        terraform_json = json.load(file)

    blueprint = TerraformParser().build_blueprint(terraform_json)

    graph = InfrastructureGraphBuilder().build_graph(blueprint)

    graph_service = GraphService()

    assert (
        graph_service.dependency_count(
            graph,
            "aws_vpc.main",
        )
        == 3
    )

    assert (
        graph_service.dependency_count(
            graph,
            "aws_instance.web",
        )
        == 0
    )
