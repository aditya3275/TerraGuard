from pydantic import BaseModel

from app.models.graph_position import GraphPosition


class ResourceMetrics(BaseModel):
    """
    Deterministic graph metrics for a single resource.
    """

    resource: str

    dependency_count: int

    blast_radius: int

    graph_position: GraphPosition

    resource_weight: int
