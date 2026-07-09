from abc import ABC, abstractmethod

from app.models import (
    AnalysisReport,
    InfraBlueprint,
)


class Analyzer(ABC):
    """
    Base interface for every TerraGuard analyzer.
    """

    @abstractmethod
    def analyze(
        self,
        blueprint: InfraBlueprint,
    ) -> AnalysisReport:
        """
        Executes the analyzer and returns
        a typed report.
        """
        pass
