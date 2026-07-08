from typing import Any

from pydantic import BaseModel


class OutputChange(BaseModel):
    """
    Represents one Terraform output.
    """

    name: str

    value: Any

    sensitive: bool = False
