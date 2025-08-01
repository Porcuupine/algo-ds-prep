from collections import Counter

import pytest


class TestIsomorphicStrings:
    """
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
    Example 1:
    Input: s = "egg", t = "add"
    Output: true
    Explanation:
    The strings s and t can be made identical by:
    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.
    Example 2:
    Input: s = "foo", t = "bar"
    Output: false
    Explanation:
    The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.
    Example 3:
    Input: s = "paper", t = "title"
    Output: true
    Constraints:
    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.
    """

    def isomorphic_strings(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}

        for a, b in zip(s, t):
            if (a in s_to_t and s_to_t[a] != b) or (b in t_to_s and t_to_s[b] != a):
                return False
            s_to_t[a] = b
            t_to_s[b] = a

        return True


    @pytest.mark.parametrize("s, t, expected",
                             [
                                 ("egg", "add", True),
                                 ("foo", "bar", False),
                                 ("paper", "title", True),

                             ])
    def test_isomorphic_strings(self, s, t, expected):
        self.isomorphic_strings(s, t) == expected
