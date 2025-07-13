import pytest


class TestThreeSum:
    """
    Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]] such that i ≠ j ≠ k and nums[i] + nums[j] + nums[k] == 0. Triplets should not be repeated in the output.
    """

    def three_sum(self, nums: list[int]) -> list[int]:
        nums.sort() # Sort the array (ascending)

        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # Skip identical values of nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # ---- Duplicate guards for left & right ----
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

    @pytest.mark.parametrize("nums, expect", [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
    ])
    def test_three_sum(self, nums, expect):
        res = self.three_sum(nums)
        assert res == expect
