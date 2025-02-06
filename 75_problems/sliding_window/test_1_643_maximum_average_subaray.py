import pytest


class TestMaximumAverageSubaray:
    """643. Maximum Average Subarray I
    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

    Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
    Example 2:

    Input: nums = [5], k = 1
    Output: 5.00000
    Constraints:
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104"""

    def max_average_subaray(self, nums: list[int], k: int):
        """
        [1,12,-5,-6,50,3], k = 4
         l        r        sum = 13
            l       r      sum = 13 - 12 + 50 = 51
               l       r   sum = 51 -(-5) + 3 = 59
        """
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            if currSum > maxSum:
                maxSum = currSum

        return maxSum / k

    @pytest.mark.parametrize(
        'nums, k, expected', [
            ([1, 12, -5, -6, 50, 3], 4, 12.75),
            ([5], 1, 5)
        ]
    )
    def test_max_average_subaray(self, nums, k, expected):
        assert self.max_average_subaray(nums, k) == expected
