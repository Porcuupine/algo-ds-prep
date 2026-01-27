import pytest


class TestLongestConsecutive_sequence:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.
    Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
    Example 3:
    Input: nums = [1,0,1,2]
    Output: 3
    Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    """

    def longest_consecutive_sequence(self, nums: list[int]) -> int:

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # only start counting if num is the start of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

    @pytest.mark.parametrize("nums, expected", [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
    ])
    def test_longest_consecutive_sequence(self, nums, expected):
        assert self.longest_consecutive_sequence(nums) == expected
