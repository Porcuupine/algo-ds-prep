import pytest


class TestDecodeString:
    """
    Given an encoded string, return its decoded string.
    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
    You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
    The test cases are generated so that the length of the output will never exceed 105.
    Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"
    Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
    Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
    """

    def decode_string(self, s: str) -> str:
        stack: list = []
        chars = "abc"
        digits = "123"

        s = s.replace("]", "")
        data = s.split("[")

        count = 1

        for char in data:
            if char in chars:
                for i in range(count):
                    stack.append(char)
            elif char in digits:
                count = int(char)
            else:
                for c in char:
                    if c in chars:
                        for i in range(count):
                            stack.append(c)
                    elif c in digits:
                        count = int(c)

        return "".join(stack)

    @pytest.mark.parametrize("s, expected", [
        ("3[a]2[bc]", "aaabcbc"),
    ])
    def test_decode_string(self, s: str, expected: str):
        assert self.decode_string(s) == expected
