from collections import Counter

import pytest


class TestValidAnagram:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:
    Input: s = "rat", t = "car"
    Output: false
    Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
    Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
    """

    def is_anagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1
        return True

    @pytest.mark.parametrize("s, t, expected", [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ])
    def test_is_anagram(self, s, t, expected):
        assert self.is_anagram(s, t) == expected
