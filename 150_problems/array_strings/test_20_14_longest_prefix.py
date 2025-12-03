import pytest


class TestLongestPrefix:
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
    """

    def longest_prefix(self, strs: list[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]

        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]

    @pytest.mark.parametrize("strs, expected", [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ])
    def test_longest_prefix(self, strs, expected):
        assert self.longest_prefix(strs) == expected
