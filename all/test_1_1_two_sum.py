from curses.ascii import isxdigit

import pytest


class TestTwoSum:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

    Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
    """

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # # brute force
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
        #
        # hash map:
        s: dict[int, int] = {}
        for idx, ele in enumerate(nums):
            if target - ele in s:
                return [s[target - ele], idx]
            s[ele] = idx

        return []

    @pytest.mark.parametrize(
        "nums, target, expected", [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ])
    def test_two_sum(self, nums: list, target, expected: list):
        res = self.two_sum(nums, target)
        assert res == expected
