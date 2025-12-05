import pytest


class TestTextJustification:
    """
    Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
    For the last line of text, it should be left-justified, and no extra space is inserted between words.
    Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.
    Example 1:
    Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    Output:
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]
    Example 2:
    Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
    Output:
    [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
    Note that the second line is also left-justified because it contains only one word.
    Example 3:
    Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
    Output:
    [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]
    Constraints:
    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
    """

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0

        while i < len(words):
            # 1) Determine how many words fit in this line
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            num_words = j - i
            total_chars = sum(len(w) for w in words[i:j])

            # 2) If last line OR single word → left-justify
            if j == len(words) or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
                res.append(line)
            else:
                # 3) Fully justify
                spaces = maxWidth - total_chars
                gaps = num_words - 1
                base = spaces // gaps
                extra = spaces % gaps

                line = ""
                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (base + (1 if k - i < extra else 0))
                line += words[j - 1]

                res.append(line)

            i = j

        return res

    @pytest.mark.parametrize(
        "words,maxWidth,expected",
        [
            (
                ["This", "is", "an", "example", "of", "text", "justification."],
                16,
                [
                    "This    is    an",
                    "example  of text",
                    "justification.  "
                ]
            ),
            (
                ["What", "must", "be", "acknowledgment", "shall", "be"],
                16,
                [
                    "What   must   be",
                    "acknowledgment  ",
                    "shall be        "
                ]
            ),
            (
                ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                 "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],
                20,
                [
                    "Science  is  what we",
                    "understand      well",
                    "enough to explain to",
                    "a  computer.  Art is",
                    "everything  else  we",
                    "do                  ",
                ]
            ),
        ]
    )
    def test_fullJustify(self, words, maxWidth, expected):
        assert self.fullJustify(words, maxWidth) == expected
