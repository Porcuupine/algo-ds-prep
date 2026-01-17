from collections import defaultdict

import pytest


class TestGroupAnagrams:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Explanation:
    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
    Example 2:
    Input: strs = [""]
    Output: [[""]]
    Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
    Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
    """

    def group_anagrags(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())

    @pytest.mark.parametrize("strs, expected", [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
    ])
    def test_group_anagrams(self, strs, expected):
        assert self.group_anagrags(strs) == expected
