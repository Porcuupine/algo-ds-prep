import pytest

class TestFindPairWithGivinSum:
    """
    Given an array nums and a number target, return True if any two different numbers in nums add up to target, else return False.
    """
    def find_pair_with_given_sum(self, nums: list, target: int) -> bool:
        n = len(nums)
        for i in range(n-1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return True
        return False

    @pytest.mark.parametrize("nums, target, expect",[
        ([1, 2, 3, 4], 5, True),
        ([1, 2, 3, 9], 8, False),
    ])
    def test_find_pair_with_given_sum(self, nums: list, target: int, expect: bool):
        res = self.find_pair_with_given_sum(nums, target)
        assert res == expect