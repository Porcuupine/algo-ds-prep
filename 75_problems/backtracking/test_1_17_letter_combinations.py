import pytest


class TestLetterCombinations:
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    Example 2:
    Input: digits = ""
    Output: []
    Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]
    Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
    """

    import pytest

    def letter_combinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for char in phone[digits[index]]:
                backtrack(index + 1, path + [char])

        backtrack(0, [])
        return res

    @pytest.mark.parametrize("digits, expected", [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),  # edge case
        ("2", ["a", "b", "c"]),
    ])
    def test_letterCombinations(self, digits, expected):
        assert sorted(self.letter_combinations(digits)) == sorted(expected)
