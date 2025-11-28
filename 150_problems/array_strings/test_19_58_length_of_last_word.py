import pytest


class TestLenghtOfLastWord:
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    A word is a maximal substring consisting of non-space characters only.
    Example 1:
    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.
    Example 2:
    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.
    Example 3:
    Input: s = "luffy is still joyboy"
    Output: 6
    Explanation: The last word is "joyboy" with length 6.
    Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
    """

    def length_of_word(self, s: str) -> int:
        return len(s.split()[-1])
        # i = len(s) - 1
        #
        # # trim from right side
        # while i >= 0 and s[i] == " ":
        #     i -= 1
        #
        # # count from end till the first " ":
        # length = 0
        # while i >= 0 and s[i] != " ":
        #     length += 1
        #     i -= 1
        #
        # return length

    @pytest.mark.parametrize("s, expected", [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ]
                             )
    def test_length_of_word(self, s, expected):
        assert self.length_of_word(s) == expected
