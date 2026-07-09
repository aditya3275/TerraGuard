from abc import ABC, abstractmethod

from app.models import (
    InfraBlueprint,
    InfrastructureGraph,
)


class GraphBuilder(ABC):
    """
    Base class for building an InfrastructureGraph
    from an InfraBlueprint.
    """

    @abstractmethod
    def build_graph(
        self,
        blueprint: InfraBlueprint,
    ) -> InfrastructureGraph:
        raise NotImplementedError
