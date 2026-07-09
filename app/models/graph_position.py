from enum import Enum


class GraphPosition(str, Enum):
    ROOT = "Root"
    INTERMEDIATE = "Intermediate"
    LEAF = "Leaf"
