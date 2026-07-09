from typing import List

from pydantic import BaseModel, Field

from app.models.configuration import Configuration
from app.models.metadata import Metadata
from app.models.output_change import OutputChange
from app.models.resource_change import ResourceChange


class InfraBlueprint(BaseModel):
    """
    Canonical representation of an infrastructure change.

    Produced by TerraformParser.
    """

    metadata: Metadata

    configuration: Configuration

    resource_changes: List[ResourceChange] = Field(default_factory=list)

    outputs: List[OutputChange] = Field(default_factory=list)
