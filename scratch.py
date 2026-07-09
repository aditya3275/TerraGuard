from app.analyzers.checkov.analyzer import CheckovAnalyzer
from app.analyzers.checkov.parser import CheckovParser

from app.graph.algorithms.criticality import (
    CriticalityAnalyzer,
)
from app.graph.infrastructure_graph_builder import (
    InfrastructureGraphBuilder,
)
from app.parser.terraform_parser import (
    TerraformParser,
)

from app.correlation.resource_correlator import (
    ResourceCorrelator,
)

from app.renderers.resource_risk_renderer import (
    ResourceRiskRenderer,
)

import json

with open("terraform_examples/basic_vpc/plan.json") as file:

    terraform_json = json.load(file)

blueprint = TerraformParser().build_blueprint(terraform_json)

graph = InfrastructureGraphBuilder().build_graph(blueprint)

criticality = CriticalityAnalyzer().analyze(graph)

security = CheckovParser().parse(
    CheckovAnalyzer().analyze("terraform_examples/basic_vpc")
)

risk = ResourceCorrelator().correlate(
    criticality,
    security,
)

print(ResourceRiskRenderer().render(risk))
