from collections import Counter, defaultdict

import pytest


class TestRansomNote:
    """
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.
    Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false
    Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false
    Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true
    Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
    """

    def ransom_note(self, ransomNote: str, magazine: str) -> bool:
        # ransom_count = Counter(ransomNote)
        # magazine_count = Counter(magazine)
        #
        # for char, count in ransom_count.items():
        #     if magazine_count[char] < count:
        #         return False
        # return True
        counts = defaultdict(int)

        # Count letters in magazine
        for ch in magazine:
            counts[ch] += 1

        # Use letters for ransomNote
        for ch in ransomNote:
            if counts[ch] == 0:
                return False
            counts[ch] -= 1

        return True

    @pytest.mark.parametrize("ransom_note, magazine, expected",
                             [
                                 ("a", "b", False),
                                 ("aa", "aab", True),
                             ])
    def test_ransom_note(self, ransom_note, magazine, expected):
        assert self.ransom_note(ransom_note, magazine) == expected
