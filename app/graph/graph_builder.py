from app.models import (
    InfrastructureGraph,
    TerraformPlan,
)


class GraphBuilder:
    """
    Converts a TerraformPlan into an InfrastructureGraph.
    """

    def build(self, plan: TerraformPlan) -> InfrastructureGraph:
        """
        Build the infrastructure graph.

        For Sprint 1 this simply returns the graph already
        attached to the plan.

        In Sprint 2 this method will construct nodes and edges.
        """

        return plan.graph
