from pydantic import BaseModel


class Metadata(BaseModel):
    """
    Metadata about the Terraform execution plan.
    """

    terraform_version: str

    format_version: str

    applyable: bool

    complete: bool

    errored: bool
