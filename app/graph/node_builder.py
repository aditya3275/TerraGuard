from app.models import (
    InfraBlueprint,
    InfrastructureResource,
)


class NodeBuilder:
    """
    Builds graph nodes from an InfraBlueprint.
    """

    def build_nodes(
        self,
        blueprint: InfraBlueprint,
    ) -> dict[str, InfrastructureResource]:

        nodes = {}

        for change in blueprint.resource_changes:

            resource = InfrastructureResource(
                id=change.address,
                name=change.resource_name,
                type=change.resource_type,
                provider=change.provider,
                action=change.actions[0],
                attributes=change.after,
                tags=change.after.get(
                    "tags",
                    {},
                ),
            )

            nodes[resource.id] = resource

        return nodes
