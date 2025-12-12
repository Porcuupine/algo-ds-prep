import pytest


class TestMinWindowSubstring:
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
    The testcases will be generated such that the answer is unique.
    Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
    Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.
    Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.
    """

    def min_window_bruteforce(self, s, t):
        from collections import Counter
        need = Counter(t)
        n = len(s)
        best = ""

        for i in range(n):
            count = need.copy()
            missing = len(t)
            for j in range(i, n):
                if count[s[j]] > 0:
                    missing -= 1
                count[s[j]] -= 1

                if missing == 0:
                    window = s[i:j + 1]
                    if best == "" or len(window) < len(best):
                        best = window
                    break

        return best

    @pytest.mark.parametrize("s, t, expected", [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ])
    def test_min_window(self, s, t, expected):
        assert self.min_window_bruteforce(s, t) == expected
