from pydantic import BaseModel

from app.models.criticality_level import (
    CriticalityLevel,
)


class CriticalityItem(BaseModel):

    resource: str

    score: int

    level: CriticalityLevel

    dependency_count: int

    blast_radius: int

    rank: int
