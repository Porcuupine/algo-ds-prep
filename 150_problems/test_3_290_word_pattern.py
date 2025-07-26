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
    def word_pattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        p_to_s = {}
        s_to_p = {}

        for a, b in zip(pattern, s_list):
            if (a in p_to_s and p_to_s[a] != b) or (b in s_to_p and s_to_p[b] != a):
                return False
            p_to_s[a] = b
            s_to_p[b] = a

        return True


    @pytest.mark.parametrize("pattern, s, expected", [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
    ])
    def test_word_pattern(self, pattern, s, expected):
        assert self.word_pattern(pattern, s) == expected


