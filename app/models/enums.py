from enum import Enum


class CloudProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    KUBERNETES = "kubernetes"
    UNKNOWN = "unknown"


class ResourceAction(str, Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    NO_OP = "no-op"


class RelationshipType(str, Enum):
    DEPENDS_ON = "depends_on"

    REFERENCES = "references"

    ATTACHED_TO = "attached_to"

    ROUTES_TO = "routes_to"

    ASSUMES_ROLE = "assumes_role"

    CONNECTED_TO = "connected_to"
