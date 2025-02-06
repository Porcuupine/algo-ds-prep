from collections import Counter

import pytest


class TestEqualRowAndColumnPairs:
    """
    2352. Equal Row and Column Pairs
    Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
    A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

    Example 1:
    Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
    Output: 1
    Explanation: There is 1 equal row and column pair:
    - (Row 2, Column 1): [2,7,7]
    Example 2:
    Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    Output: 3
    Explanation: There are 3 equal row and column pairs:
    - (Row 0, Column 0): [3,1,2,2]
    - (Row 2, Column 2): [2,4,2,2]
    - (Row 3, Column 2): [2,4,2,2]
    Constraints:
    n == grid.length == grid[i].length
    1 <= n <= 200
    1 <= grid[i][j] <= 105
    """

    def equal_row_and_column_pairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_counts = Counter(tuple(row) for row in grid)
        columns = zip(*grid)
        count = 0
        for col in columns:
            count += row_counts[tuple(col)]

        return count


    @pytest.mark.parametrize(
        'grid, expected', [
            ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
            ([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 3),
        ]
    )
    def test_equal_row_and_column_pairs(self, grid, expected):
        assert self.equal_row_and_column_pairs(grid) == expected
