from app.models import (
    CloudProvider,
    InfraBlueprint,
    Metadata,
    OutputChange,
    ResourceAction,
    ResourceChange,
)

from app.parser.base import IaCParser


class TerraformParser(IaCParser):
    """
    Parses Terraform JSON into an InfraBlueprint.
    """

    def build_blueprint(
        self,
        terraform_json: dict,
    ) -> InfraBlueprint:

        metadata = self._build_metadata(terraform_json)

        resource_changes = self._build_resource_changes(terraform_json)

        outputs = self._build_outputs(terraform_json)

        return InfraBlueprint(
            metadata=metadata,
            resource_changes=resource_changes,
            outputs=outputs,
        )

    def _build_metadata(self, terraform_json: dict) -> Metadata:
        return Metadata(
            terraform_version=terraform_json.get("terraform_version", ""),
            format_version=terraform_json.get("format_version", ""),
            applyable=terraform_json.get(
                "applyable",
                False,
            ),
            complete=terraform_json.get(
                "complete",
                False,
            ),
            errored=terraform_json.get(
                "errored",
                False,
            ),
        )

    def _build_resource_changes(
        self,
        terraform_json: dict,
    ) -> list[ResourceChange]:

        resource_changes = []

        for resource in terraform_json.get(
            "resource_changes",
            [],
        ):

            provider = self._detect_provider(resource.get("provider_name", ""))

            actions = self._convert_actions(resource["change"]["actions"])

            resource_changes.append(
                ResourceChange(
                    address=resource["address"],
                    mode=resource["mode"],
                    resource_type=resource["type"],
                    resource_name=resource["name"],
                    provider=provider,
                    actions=actions,
                    before=resource["change"]["before"] or {},
                    after=resource["change"]["after"] or {},
                )
            )

        return resource_changes

    def _build_outputs(
        self,
        terraform_json: dict,
    ) -> list[OutputChange]:

        outputs = []

        output_changes = terraform_json.get(
            "output_changes",
            {},
        )

        for name, value in output_changes.items():
            outputs.append(
                OutputChange(
                    name=name,
                    value=value.get("after"),
                    sensitive=value.get(
                        "after_sensitive",
                        False,
                    ),
                )
            )

        return outputs

    def _detect_provider(
        self,
        provider_name: str,
    ) -> CloudProvider:

        if "aws" in provider_name:
            return CloudProvider.AWS

        if "azurerm" in provider_name:
            return CloudProvider.AZURE

        if "google" in provider_name:
            return CloudProvider.GCP

        return CloudProvider.UNKNOWN

    def _convert_actions(
        self,
        actions: list[str],
    ) -> list[ResourceAction]:

        return [ResourceAction(action) for action in actions]
