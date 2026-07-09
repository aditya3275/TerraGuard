from collections import defaultdict

from pydantic import BaseModel, Field

from app.models import (
    CriticalityItem,
    CriticalityLevel,
)


class CriticalityReport(BaseModel):
    """
    Final deterministic criticality report.

    This is the single source of truth consumed by
    GitHub, CLI, Dashboard and the LLM layer.
    """

    resources: list[CriticalityItem] = Field(default_factory=list)

    def grouped_resources(
        self,
    ) -> dict[
        CriticalityLevel,
        list[CriticalityItem],
    ]:

        groups = defaultdict(list)

        for resource in self.resources:
            groups[resource.level].append(resource)

        return dict(groups)

    def summary(
        self,
    ) -> dict[
        CriticalityLevel,
        int,
    ]:

        summary = {
            CriticalityLevel.CRITICAL: 0,
            CriticalityLevel.HIGH: 0,
            CriticalityLevel.MEDIUM: 0,
            CriticalityLevel.LOW: 0,
        }

        for resource in self.resources:
            summary[resource.level] += 1

        return summary

    def highest_risk(
        self,
    ) -> CriticalityItem | None:

        if not self.resources:
            return None

        return self.resources[0]

    def top_resources(
        self,
        limit: int = 5,
    ) -> list[CriticalityItem]:

        return self.resources[:limit]

    def total_resources(
        self,
    ) -> int:

        return len(self.resources)
