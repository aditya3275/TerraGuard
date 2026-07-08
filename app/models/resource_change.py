from typing import Any, Dict, List

from pydantic import BaseModel, Field

from app.models.enums import (
    CloudProvider,
    ResourceAction,
)


class ResourceChange(BaseModel):
    """
    Represents a single resource change
    from a Terraform execution plan.
    """

    address: str

    mode: str

    resource_type: str

    resource_name: str

    provider: CloudProvider

    actions: List[ResourceAction] = Field(default_factory=list)

    before: Dict[str, Any] = Field(default_factory=dict)

    after: Dict[str, Any] = Field(default_factory=dict)
