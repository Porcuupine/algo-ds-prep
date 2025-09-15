from collections import defaultdict

import pytest


class TestReorderRoutes:
    """
    There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
    Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
    This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
    Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
    It's guaranteed that each city can reach city 0 after reorder.

    Example 1:
    Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    Output: 3
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
    Example 2:
    Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
    Output: 2
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
    Example 3:
    Input: n = 3, connections = [[1,0],[2,0]]
    Output: 0
    Constraints:
    2 <= n <= 5 * 104
    connections.length == n - 1
    connections[i].length == 2
    0 <= ai, bi <= n - 1
    ai != bi
    """

    def reorder_routes(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)

        # Build graph: mark direction (1 if original is from->to)
        for a, b in connections:
            graph[a].append((b, 1))  # forward edge
            graph[b].append((a, 0))  # reverse edge (already toward 0)

        visited = set()

        def dfs(city: int) -> int:
            visited.add(city)
            changes = 0
            for nei, needs_reversal in graph[city]:
                if nei not in visited:
                    # if the edge was going away from 0, we need to reverse it
                    changes += needs_reversal + dfs(nei)
            return changes

        return dfs(0)

    @pytest.mark.parametrize("n, connections, expected", [
        (6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]], 3),
        (5, [[1, 0], [1, 2], [3, 2], [3, 4]], 2),
    ])
    def test_reorder_routes(self, n, connections, expected):
        assert self.reorder_routes(n, connections) == expected
