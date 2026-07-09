from app.graph.builder import GraphBuilder
from app.graph.node_builder import NodeBuilder
from app.graph.edge_builder import EdgeBuilder

from app.models import (
    InfraBlueprint,
    InfrastructureGraph,
)


class InfrastructureGraphBuilder(GraphBuilder):
    """
    Orchestrates graph construction.
    """

    def __init__(self):

        self.node_builder = NodeBuilder()

        self.edge_builder = EdgeBuilder()

    def build_graph(
        self,
        blueprint: InfraBlueprint,
    ) -> InfrastructureGraph:

        graph = InfrastructureGraph()

        graph.nodes = self.node_builder.build_nodes(blueprint)

        graph.edges = self.edge_builder.build_edges(blueprint)

        return graph
