from typing import List
from pydantic import BaseModel, Field

from app.models.resource import InfrastructureResource
from app.models.relationship import InfrastructureRelationship


class InfrastructureGraph(BaseModel):
    """
    Represents the parsed infrastructure graph.
    """

    resources: List[InfrastructureResource] = Field(default_factory=list)

    relationships: List[InfrastructureRelationship] = Field(default_factory=list)
