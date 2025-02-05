import pytest


class TestMinimumSizeSubarraySum:
    """
    Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1
    Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0
    Constraints:
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104

    Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
    """

    def minimum_size_subarray_sum(self, nums: list[int], target: int):
        """
        [2, 3, 1, 2, 4, 3] t = 7
        l   r                  = 5
        l      r                = 6
        l         r             = 8
            l        r          = 10
                l    r          = 7
                l       r       = 10
                   l    r       = 9
                      l  r       = 7

        """
        curr_sum = 0
        left = 0
        min_len = float('inf')
        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0

    @pytest.mark.parametrize(
        "nums, target, expected", [
            ([2, 3, 1, 2, 4, 3], 7, 2),
            ([1, 4, 4], 4, 1),
            ([1, 1, 1, 1, 1, 1, 1, 1], 11, 0),
        ]
    )
    def test_minimum_size_subarray(self, nums, target, expected):
        assert self.minimum_size_subarray_sum(nums, target) == expected
