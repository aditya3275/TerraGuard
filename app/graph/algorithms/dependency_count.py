from app.graph.algorithms.blast_radius import (
    BlastRadiusAnalyzer,
)

from app.models import InfrastructureGraph


class DependencyCountAnalyzer:
    """
    Computes how many resources depend
    on a given resource.
    """

    def __init__(self):

        self.blast_radius = BlastRadiusAnalyzer()

    def analyze(
        self,
        graph: InfrastructureGraph,
        resource: str,
    ) -> int:

        affected = self.blast_radius.analyze(
            graph,
            resource,
        )

        return max(
            len(affected) - 1,
            0,
        )
