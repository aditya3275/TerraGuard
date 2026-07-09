from pydantic import BaseModel


class SecurityFinding(BaseModel):
    """
    Represents a single security finding produced
    by an analyzer such as Checkov.
    """

    check_id: str

    title: str

    severity: str

    resource: str

    file_path: str | None = None

    guideline: str | None = None
