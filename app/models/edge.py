from pydantic import BaseModel, Field

from app.models.enums import RelationshipType


class InfrastructureEdge(BaseModel):
    """
    Represents a connection (edge) between two infrastructure nodes.
    """

    source: str = Field(
        ...,
        description="Source node ID",
    )

    target: str = Field(
        ...,
        description="Target node ID",
    )

    relationship_type: RelationshipType = Field(
        ...,
        description="Relationship between the nodes",
    )
