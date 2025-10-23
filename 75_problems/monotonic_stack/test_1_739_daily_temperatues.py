import pytest


class TestDeilyTemperatures:
    """
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]
    Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]
    Constraints:
    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100
    """

    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        # bruteforce:
        # n = len(temperatures)
        # res = [0] * n
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res

        # stack:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # check if the current temp is warmer than previous ones
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            stack.append(i)

        return res

    @pytest.mark.parametrize("temperatures, expected", [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ])
    def test_daily_temperatures(self, temperatures, expected):
        assert self.daily_temperatures(temperatures) == expected
