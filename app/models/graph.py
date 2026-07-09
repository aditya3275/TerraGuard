from collections import defaultdict
from typing import Dict, List

from pydantic import BaseModel, Field

from app.models.edge import InfrastructureEdge
from app.models.resource import InfrastructureResource


class InfrastructureGraph(BaseModel):
    """
    Graph representation of the infrastructure.

    Nodes are indexed by resource address.
    """

    nodes: Dict[str, InfrastructureResource] = Field(default_factory=dict)

    edges: List[InfrastructureEdge] = Field(default_factory=list)

    def adjacency(self) -> dict[str, list[str]]:
        """
        source -> targets
        """

        graph = defaultdict(list)

        for edge in self.edges:
            graph[edge.source].append(edge.target)

        return dict(graph)

    def reverse_adjacency(self) -> dict[str, list[str]]:
        """
        target -> dependents
        """

        graph = defaultdict(list)

        for edge in self.edges:
            graph[edge.target].append(edge.source)

        return dict(graph)
