from collections import deque

from app.models import InfrastructureGraph


class BlastRadiusAnalyzer:
    """
    Finds every resource affected by a change.
    """

    def analyze(
        self,
        graph: InfrastructureGraph,
        start_node: str,
    ) -> list[str]:

        reverse = graph.reverse_adjacency()

        visited = set()

        queue = deque([start_node])

        while queue:

            current = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            for neighbour in reverse.get(
                current,
                [],
            ):
                queue.append(neighbour)

        return sorted(visited)
