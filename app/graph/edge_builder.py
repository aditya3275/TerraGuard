from app.models import (
    InfraBlueprint,
    InfrastructureEdge,
    RelationshipType,
)


class EdgeBuilder:
    """
    Builds graph edges by analyzing
    Terraform resource references.
    """

    def build_edges(
        self,
        blueprint: InfraBlueprint,
    ) -> list[InfrastructureEdge]:

        edges = []

        for resource in blueprint.configuration.resources:

            source = resource.address

            for expression in resource.expressions.values():

                for reference in expression.references:

                    target = reference.removesuffix(".id")

                    edge = InfrastructureEdge(
                        source=source,
                        target=target,
                        relationship_type=RelationshipType.REFERENCES,
                    )

                    if edge not in edges:
                        edges.append(edge)

        return edges
