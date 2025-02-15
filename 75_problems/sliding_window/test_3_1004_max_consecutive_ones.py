import pytest


class TestMaxConsecutiveOnes:
    """1004. Max Consecutive Ones III
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

    Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length"""

    def max_consecutive_ones(self, nums, k):
        """
        [1,1,1,0,0,0,1,1,1,1,0]   k = 2
         l         r              k = -1:  currNum = 6 - 1
           l       r
             l     r
               l   r
                 l   r            k = 0    currNum = 3 - 1
                 l           r    k = -1   currNum = 7 - 1
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1

    @pytest.mark.parametrize(
        'nums, k, expected', [
            ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
            # ([1, 0, 0, 0, 1, 0, 1], 2, 4)
        ]
    )
    def test_max_consecutive_ones(self, nums, k, expected):
        assert self.max_consecutive_ones(nums, k) == expected
