from pydantic import BaseModel, Field

from app.models.enums import RelationshipType


class InfrastructureRelationship(BaseModel):
    """
    Represents a relationship between two infrastructure resources.
    """

    source: str = Field(..., description="Source resource ID")

    target: str = Field(..., description="Target resource ID")

    relationship_type: RelationshipType = Field(
        ..., description="Relationship between resources"
    )
