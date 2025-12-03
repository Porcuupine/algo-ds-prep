import pytest


class TestZigZagConvertion:
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:
    string convert(string s, int numRows);
    Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    Example 3:
    Input: s = "A", numRows = 1
    Output: "A"
    Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
    """

    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s

        rows = [""] * num_rows
        cur = 0
        direction = 1  # 1 = down, -1 = up

        for ch in s:
            rows[cur] += ch

            if cur == 0:
                direction = 1
            elif cur == num_rows - 1:
                direction = -1

            cur += direction

        return "".join(rows)

    @pytest.mark.parametrize("s, num_rows, expected", [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
    ])
    def test_convert(self, s, num_rows, expected):
        assert self.convert(s, num_rows) == expected
