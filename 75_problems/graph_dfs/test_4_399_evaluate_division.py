from collections import defaultdict

import pytest


class TestEvaluateDivision:
    """

    """

    def evaluate_division(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]]) -> list[float]:

        # build graph
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # DFS helper
        def dfs(src, dst, visited):
            if src == dst:
                return 1.0
            visited.add(src)
            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    res = dfs(neighbor, dst, visited)
                    if res != -1.0:
                        return res * weight
            return -1.0

        # Answer queries
        result = []
        for a, b in queries:
            if a not in queries:
                if a not in graph or b not in graph:
                    result.append(-1.0)
                else:
                    result.append(dfs(a, b, set()))
        return result

    @pytest.mark.parametrize("equations, values, queries, expected",
                             [
                                 (
                                     [["a", "b"], ["b", "c"]],
                                     [2.0, 3.0],
                                     [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
                                     [6.0, 0.5, -1.0, 1.0, -1.0]
                                 ),
                                 (
                                     [["x", "y"]],
                                     [4.0],
                                     [["x", "y"], ["y", "x"], ["x", "x"], ["y", "y"], ["x", "z"]],
                                     [4.0, 0.25, 1.0, 1.0, -1.0]
                                 )
                             ])
    def test_evaluate_division(self, equations, values, queries, expected):
        assert self.evaluate_division(equations, values, queries) == pytest.approx(expected)
