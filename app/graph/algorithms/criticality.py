from app.graph.algorithms.blast_radius import (
    BlastRadiusAnalyzer,
)
from app.graph.algorithms.dependency_count import (
    DependencyCountAnalyzer,
)
from app.graph.algorithms.graph_position import (
    GraphPositionAnalyzer,
)
from app.graph.algorithms.resource_weight import (
    RESOURCE_WEIGHTS,
)

from app.models import (
    CriticalityItem,
    CriticalityLevel,
    CriticalityReport,
    GraphPosition,
    InfrastructureGraph,
)


class CriticalityAnalyzer:
    """
    Computes deterministic infrastructure criticality.
    """

    def __init__(self):

        self.dependency = DependencyCountAnalyzer()

        self.blast = BlastRadiusAnalyzer()

        self.position = GraphPositionAnalyzer()

    def analyze(
        self,
        graph: InfrastructureGraph,
    ) -> CriticalityReport:

        items = []

        max_dependency = max(
            (self.dependency.analyze(graph, resource) for resource in graph.nodes),
            default=1,
        )

        for resource_id, resource in graph.nodes.items():

            dependency_count = self.dependency.analyze(
                graph,
                resource_id,
            )

            blast_radius = len(
                self.blast.analyze(
                    graph,
                    resource_id,
                )
            )

            graph_position = self.position.analyze(
                graph,
                resource_id,
            )

            dependency_score = (dependency_count / max_dependency) * 100

            position_score = {
                GraphPosition.ROOT: 100,
                GraphPosition.INTERMEDIATE: 70,
                GraphPosition.LEAF: 40,
            }[graph_position]

            resource_weight = RESOURCE_WEIGHTS.get(
                resource.type,
                50,
            )

            score = int(
                (0.5 * dependency_score)
                + (0.3 * position_score)
                + (0.2 * resource_weight)
            )

            if score >= 90:
                level = CriticalityLevel.CRITICAL
            elif score >= 70:
                level = CriticalityLevel.HIGH
            elif score >= 50:
                level = CriticalityLevel.MEDIUM
            else:
                level = CriticalityLevel.LOW

            items.append(
                CriticalityItem(
                    resource=resource_id,
                    score=score,
                    level=level,
                    dependency_count=dependency_count,
                    blast_radius=blast_radius,
                    rank=0,
                )
            )

        items.sort(
            key=lambda item: item.score,
            reverse=True,
        )

        for rank, item in enumerate(
            items,
            start=1,
        ):
            item.rank = rank

        return CriticalityReport(resources=items)
