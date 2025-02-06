from collections import Counter

import pytest


class TestUniqueNumberOfOccurrences:
    """
    1207. Unique Number of Occurrences
    Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

    Example 1:
    Input: arr = [1,2,2,1,1,3]
    Output: true
    Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
    Example 2:
    Input: arr = [1,2]
    Output: false
    Example 3:
    Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    Output: true
    Constraints:
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
    """

    def unique_number_of_occurences(self, arr: list[int]) -> bool:

        freq = Counter(arr)
        occurrences = list(freq.values())  # from dict to list
        return len(occurrences) == len(set(occurrences))  # compare len of a list with len of a set

    @pytest.mark.parametrize(
        'arr, expected', [
            ([1, 2, 2, 1, 1, 5], True),
            ([1, 2], False),
            ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
        ]
    )
    def test_unique_number_of_occurences(self, arr: list[int], expected: bool):
        assert self.unique_number_of_occurences(arr) == expected
