from enum import Enum


class DecisionSummary(str, Enum):
    """
    Final deployment recommendation.
    """

    APPROVE = "APPROVE"

    WARN = "WARN"

    BLOCK = "BLOCK"
