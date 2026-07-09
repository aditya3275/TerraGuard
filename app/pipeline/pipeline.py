from app.graph.algorithms.criticality import (
    CriticalityAnalyzer,
)
from app.graph.infrastructure_graph_builder import (
    InfrastructureGraphBuilder,
)
from app.parser.terraform_parser import (
    TerraformParser,
)
from app.renderers.markdown_renderer import (
    MarkdownRenderer,
)


class TerraGuardPipeline:
    """
    Main orchestration pipeline for TerraGuard.
    """

    def __init__(self):

        self.parser = TerraformParser()

        self.graph_builder = InfrastructureGraphBuilder()

        self.criticality = CriticalityAnalyzer()

        self.renderer = MarkdownRenderer()

    def run(
        self,
        terraform_json: dict,
    ) -> str:

        blueprint = self.parser.build_blueprint(terraform_json)

        graph = self.graph_builder.build_graph(blueprint)

        report = self.criticality.analyze(graph)

        return self.renderer.render(report)
