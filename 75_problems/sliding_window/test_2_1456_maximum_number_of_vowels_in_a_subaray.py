import pytest


class TestMaxNumberOfVowels:
    """1456. Maximum Number of Vowels in a Substring of Given Length
    Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
    Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.
    Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.
    Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.
    Constraints:
    1 <= s.length <= 105
    s consists of lowercase English letters.
    1 <= k <= s.length"""

    def max_number_of_vowels(self, s: str, k: int):
        """
        "abciiidef" k = 3
         l r    count = 1 // because just 1 vowel
          l r   count = 1 // because "i" was added and "a" was deleted
           l r  count = 2 // "i" was added
            l r count = 3 // "i" was added
             l r  count = 2 //"i" was deleted
              l r  count = 2 // "e" was added and "i" was deleted
               l r  count = 1 // "i" was deleted
        """
        vowels = ("a", "e", "i", "o", "u")
        currSum = maxSum = sum([1 for x in s[:k] if x in vowels])
        for i in range(k, len(s)):
            currSum += (s[i] in vowels) - (s[i - k] in vowels)
            if currSum > maxSum:
                maxSum = currSum

        return maxSum

    @pytest.mark.parametrize(
        's, k, expected', [
            ('abciiidef', 3, 3),
            ('aeiou', 2, 2),
        ]
    )
    def test_max_number_of_vowels(self, s, k, expected):
        assert self.max_number_of_vowels(s, k) == expected
