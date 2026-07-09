from typing import List

from pydantic import BaseModel, Field


class Expression(BaseModel):
    """
    Represents a Terraform expression.
    """

    references: List[str] = Field(default_factory=list)
