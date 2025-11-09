from operator import truediv

import pytest


class TestJumpGame:
    """
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.
    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
    Constraints:
    1 <= nums.length <= 104
    0 <= nums[i] <= 105
    """

    def can_jump(self, nums: list[int], i: int = 0) -> bool:

        # # brute solution O(2^n) time and O(n) space
        # if i > len(nums) - 1:
        #     return True
        # for jump in range(1, nums[i] + 1):
        #     if self.can_jump(nums, i + jump):
        #         return True
        #
        # return False

        # greedy O(n) time and O(1) space:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False  # can't even reach this point
            max_reach = max(max_reach, i + jump)
        return True

    @pytest.mark.parametrize("nums, expected", [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ])
    def test_can_jump(self, nums, expected):
        assert self.can_jump(nums) == expected
