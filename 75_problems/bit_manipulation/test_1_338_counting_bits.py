import math
from itertools import count

import pytest


class TestCountingBits:
    """
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

    Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101
    Constraints:
    0 <= n <= 105
    Follow up:
    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
    """

    def counting_bits(self, n: int) -> list[int]:

        # return [bin(i).count('1') for i in range(n+1)]
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


        # return [0, 1, 1]

    @pytest.mark.parametrize("n, expected", [
        (2, [0, 1, 1]),
        (5, [0,1,1,2,1,2]),
    ])
    def test_counting_bits(self, n, expected):
        assert self.counting_bits(n) == expected
