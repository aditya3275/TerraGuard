from abc import ABC, abstractmethod

from app.models import InfraBlueprint


class IaCParser(ABC):
    """
    Base interface for Infrastructure-as-Code parsers.
    """

    @abstractmethod
    def build_blueprint(
        self,
        terraform_json: dict,
    ) -> InfraBlueprint:
        """
        Convert raw Terraform JSON into
        an InfraBlueprint.
        """
        raise NotImplementedError
