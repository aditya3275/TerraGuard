from typing import Dict, Any

from pydantic import BaseModel, Field

from app.models.enums import CloudProvider, ResourceAction


class InfrastructureResource(BaseModel):
    """
    Represents a single infrastructure resource from Terraform.
    Example:
        aws_instance.web
        aws_security_group.public
        aws_vpc.main
    """

    id: str = Field(..., description="Unique Terraform resource ID")

    name: str = Field(..., description="Logical resource name")

    type: str = Field(..., description="Terraform resource type")

    provider: CloudProvider = Field(..., description="Cloud provider")

    action: ResourceAction = Field(..., description="Terraform action")

    attributes: Dict[str, Any] = Field(default_factory=dict)

    tags: Dict[str, str] = Field(default_factory=dict)
