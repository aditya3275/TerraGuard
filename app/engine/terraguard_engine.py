import json

from app.analyzers.checkov.analyzer import CheckovAnalyzer
from app.analyzers.checkov.parser import CheckovParser
from app.correlation.resource_correlator import (
    ResourceCorrelator,
)
from app.decision.decision_engine import (
    DecisionEngine,
)
from app.graph.algorithms.criticality import (
    CriticalityAnalyzer,
)
from app.graph.infrastructure_graph_builder import (
    InfrastructureGraphBuilder,
)
from app.models import (
    AnalysisReport,
)
from app.parser.terraform_parser import (
    TerraformParser,
)


class TerraGuardEngine:
    """
    Main application entry point.

    Orchestrates the complete TerraGuard
    analysis pipeline.
    """

    def analyze(
        self,
        terraform_directory: str,
        plan_json_path: str,
    ) -> AnalysisReport:

        with open(plan_json_path) as file:
            terraform_json = json.load(file)

        blueprint = TerraformParser().build_blueprint(terraform_json)

        graph = InfrastructureGraphBuilder().build_graph(blueprint)

        criticality_report = CriticalityAnalyzer().analyze(graph)

        raw_security = CheckovAnalyzer().analyze(terraform_directory)

        security_report = CheckovParser().parse(raw_security)

        risk_report = ResourceCorrelator().correlate(
            criticality_report,
            security_report,
        )

        decision = DecisionEngine().evaluate(risk_report)

        return AnalysisReport(
            risk_report=risk_report,
            decision=decision,
        )
