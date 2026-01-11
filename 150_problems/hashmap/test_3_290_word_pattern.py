from locale import windows_locale

import pytest


class TestWordPattern:
    """
    Given a pattern and a string s, find if s follows the same pattern.
    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.
    Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
    Explanation:
    The bijection can be established as:
    'a' maps to "dog".
    'b' maps to "cat".
    Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false
    Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false
    Constraints:
    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.
    """

    def is_word_pattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for p, w in zip(pattern, words):
            # pattern -> word
            if p in p_to_w and p_to_w[p] != w:
                return False
            # word -> pattern:
            if w in w_to_p and w_to_p[w] != p:
                return False

            p_to_w[p] = w
            w_to_p[w] = p

        return True

    @pytest.mark.parametrize("pattern, s, expected", [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
    ])
    def test_is_word_pattern(self, pattern, s, expected):
        assert self.is_word_pattern(pattern, s) == expected
