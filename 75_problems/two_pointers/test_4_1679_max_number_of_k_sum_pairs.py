from itertools import count

import pytest


class TestMaxNumberOfKSumPairs:
    """You are given an integer array nums and an integer k.
    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
    Return the maximum number of operations you can perform on the array.

    Example 1:
    Input: nums = [1,2,3,4], k = 5
    Output: 2
    Explanation: Starting with nums = [1,2,3,4]:
    - Remove numbers 1 and 4, then nums = [2,3]
    - Remove numbers 2 and 3, then nums = []
    There are no more pairs that sum up to 5, hence a total of 2 operations.
    Example 2:
    Input: nums = [3,1,3,4,3], k = 6
    Output: 1
    Explanation: Starting with nums = [3,1,3,4,3]:
    - Remove the first two 3's, then nums = [1,4,3]
    There are no more pairs that sum up to 6, hence a total of 1 operation.
    Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 109
    """

    def max_number_of_sum_pairs(self, nums: list[int], k: int):
        """
        [1,2,3,4], k = 5  a = 0
        l      r   sum = 5   a = 1
        [1,2,3,4]
           l r   sum = 5   a = 2

        [3,1,3,4,3], k = 6
        sort:
        [1,3,3,3,4], k = 6    a = 0
         l       r   sum = 5  a = 0
           l     r   sum = 7  a = 0
           l   r     sum = 6  a = 1

        """
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            sum = nums[left] + nums[right]
            if sum > k:
                right -= 1
            elif sum < k:
                left += 1
            else:
                count += 1
                left += 1
                right -= 1

        return count

    @pytest.mark.parametrize(
        'nums, k, expected', [
            ([1, 2, 3, 4], 5, 2),
            ([3, 1, 3, 4, 3], 6, 1),
        ])
    def test_max_number_of_sum_pairs(self, nums: list[int], k: int, expected):
        assert self.max_number_of_sum_pairs(nums, k) == expected
