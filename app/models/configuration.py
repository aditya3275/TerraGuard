from typing import List

from pydantic import BaseModel, Field

from app.models.configuration_resource import (
    ConfigurationResource,
)


class Configuration(BaseModel):
    """
    Parsed Terraform configuration.
    """

    resources: List[ConfigurationResource] = Field(default_factory=list)
