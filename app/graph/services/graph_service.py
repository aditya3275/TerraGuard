from app.graph.algorithms.blast_radius import (
    BlastRadiusAnalyzer,
)
from app.graph.algorithms.dependency_count import (
    DependencyCountAnalyzer,
)

from app.models import InfrastructureGraph


class GraphService:
    """
    High-level API for graph analysis.
    """

    def __init__(self):

        self._blast_radius_analyzer = BlastRadiusAnalyzer()

        self._dependency_count_analyzer = DependencyCountAnalyzer()

    def blast_radius_analysis(
        self,
        graph: InfrastructureGraph,
        resource: str,
    ) -> list[str]:

        return self._blast_radius_analyzer.analyze(
            graph,
            resource,
        )

    def dependency_count(
        self,
        graph: InfrastructureGraph,
        resource: str,
    ) -> int:

        return self._dependency_count_analyzer.analyze(
            graph,
            resource,
        )
