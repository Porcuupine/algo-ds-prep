import pytest


class TestTwoSum:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # brute force
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    @pytest.mark.parametrize(
        "nums, target, expected", [
            ([2, 7, 11, 15], 9,  [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ])
    def test_two_sum(self, nums: list, target, expected: list):
        res = self.two_sum(nums, target)
        assert res == expected