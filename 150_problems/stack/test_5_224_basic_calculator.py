import pytest


class TestBasicCalculator:
    """
    Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

    Example 1:
    Input: s = "1 + 1"
    Output: 2
    Example 2:
    Input: s = " 2-1 + 2 "
    Output: 3
    Example 3:
    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23
    Constraints:
    1 <= s.length <= 3 * 105
    s consists of digits, '+', '-', '(', ')', and ' '.
    s represents a valid expression.
    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.
    """

    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_result = 0
        sign = 1  # 1 means '+', -1 means '-'

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)

            elif char in "+-":
                current_result += sign * current_number
                current_number = 0
                sign = 1 if char == "+" else -1

            elif char == "(":
                # Push result and sign before parenthesis
                stack.append(current_result)
                stack.append(sign)
                current_result = 0
                sign = 1

            elif char == ")":
                current_result += sign * current_number
                current_number = 0
                current_result *= stack.pop()  # multiply by the sign before "("
                current_result += stack.pop()  # add the result before "("

            # ignore spaces
        return current_result + sign * current_number

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("(5-(1+2))", 2),
        ("(7)-(0)+(4)", 11),
    ],
)
def test_calculate(expression, expected):
    s = TestBasicCalculator()
    assert s.calculate(expression) == expected
