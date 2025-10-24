import pytest


class TestValidParentheses:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Example 1:
    Input: s = "()"
    Output: true
    Example 2:
    Input: s = "()[]{}"
    Output: true
    Example 3:
    Input: s = "(]"
    Output: false
    Example 4:
    Input: s = "([])"
    Output: true
    Example 5:
    Input: s = "([)]"
    Output: false
    Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
    """

    def valid_parentheses(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                return False

        return not stack

    @pytest.mark.parametrize("s, expected", [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
    ])
    def test_valid_parentheses(self, s: str, expected: bool):
        assert self.valid_parentheses(s) == expected;
