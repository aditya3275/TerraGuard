from typing import Dict

from pydantic import BaseModel, Field

from app.models.expression import Expression


class ConfigurationResource(BaseModel):
    """
    Represents a single resource from the Terraform
    configuration section.
    """

    address: str

    resource_type: str

    resource_name: str

    expressions: Dict[str, Expression] = Field(default_factory=dict)
