import pytest


class TestGreatestCommonDivisorOfString:
    """1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters."""

    def greatest_common_divisor(self, str1: str, str2: str):
        if str1 + str2 != str2 + str1:
            return ''
        elif len(str1) == len(str2):
            return str1
        elif len(str1) > len(str2):
            return self.greatest_common_divisor(str1[len(str2):], str2)
        return self.greatest_common_divisor(str1, str2[len(str1):])

    @pytest.mark.parametrize(
        'str1, str2, expected', [
            ('ABCABC', 'ABC', 'ABC'),
            ('ABABAB', 'ABAB', 'AB'),
            ('LEET', 'CODE', ''),
        ]
    )
    def test_greatest_common_divisor(self, str1, str2, expected):
        assert self.greatest_common_divisor(str1, str2) == expected
