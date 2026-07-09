from app.models import (
    GraphPosition,
    InfrastructureGraph,
)


class GraphPositionAnalyzer:
    """
    Determines whether a resource is a
    ROOT, INTERMEDIATE, or LEAF node.
    """

    def analyze(
        self,
        graph: InfrastructureGraph,
        resource: str,
    ) -> GraphPosition:

        adjacency = graph.adjacency()
        reverse = graph.reverse_adjacency()

        has_dependencies = len(adjacency.get(resource, [])) > 0
        has_dependents = len(reverse.get(resource, [])) > 0

        if has_dependents and not has_dependencies:
            return GraphPosition.ROOT

        if has_dependencies and has_dependents:
            return GraphPosition.INTERMEDIATE

        return GraphPosition.LEAF
