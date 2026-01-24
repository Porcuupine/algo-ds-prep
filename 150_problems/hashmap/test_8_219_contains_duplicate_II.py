import pytest


class TestContainDuplicate:
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
    Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true
    Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true
    Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
    Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105
    """

    def contains_narby_duplicate(self, nums: list[int], k: int) -> bool:
        last_seen = {}
        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i
        return False

    @pytest.mark.parametrize("nums, k, expected", [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False)
    ])
    def test_contains_nearby_duplicate(self, nums, k, expected):
        assert self.contains_narby_duplicate(nums, k) == expected
