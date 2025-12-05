import pytest


class TestIndexOfTheFirstOccurrence:
    """
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.
    Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.
    Constraints:
    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.
    """

    def index_first_occurrence(self, haystack: str, needle: str) -> int:
        # brute force O(n * m) time and O(1) space
        # n, m = len(haystack), len(needle)
        #
        # if m == 0:
        #     return 0
        #
        # for i in range(n - m + 1):
        #     if haystack[i:i + m] == needle:
        #         return i
        # return -1
        return haystack.find(needle)

    @pytest.mark.parametrize("haystack, needle, expected", [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),

    ])
    def test_index_first_occurrence(self, haystack, needle, expected):
        assert self.index_first_occurrence(haystack, needle) == expected
