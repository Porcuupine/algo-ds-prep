import pytest

MOD = 1_000_000_007


class TestDominoTromino:
    """
    You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
    Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
    In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

    Example 1:
    Input: n = 3
    Output: 5
    Explanation: The five different ways are shown above.
    Example 2:
    Input: n = 1
    Output: 1
    Constraints:
    1 <= n <= 1000
    """

    def num_tilings(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp2 = [0] * (n + 1)

        dp[1], dp[2] = 1, 2
        dp2[2] = 1  # one way to have a missing corner at n=2

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dp2[i - 1]) % MOD
            dp2[i] = (dp2[i - 1] + dp[i - 2]) % MOD

        return dp[n]

    @pytest.mark.parametrize("n, expected", [
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 11),
        (5, 24),
        (30, 312342182),
    ])
    def test_numTilings(self, n, expected):
        assert self.num_tilings(n) == expected
