import pytest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []  # store up to 3 smallest words


class TestSearchSystem:
    """
    You are given an array of strings products and a string searchWord.
    Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
    Return a list of lists of the suggested products after each character of searchWord is typed.

    Example 1:
    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
    Example 2:
    Input: products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    Explanation: The only word "havana" will be always suggested while typing the search word.
    Constraints:
    1 <= products.length <= 1000
    1 <= products[i].length <= 3000
    1 <= sum(products[i].length) <= 2 * 104
    All the strings of products are unique.
    products[i] consists of lowercase English letters.
    1 <= searchWord.length <= 1000
    searchWord consists of lowercase English letters.
    """

    def search_suggestion_system(self, products: list[str], searchWord: str) -> list[list[str]]:
        # the simplest O(n^2) version:
        # products.sort()  # sort lexicographically
        # res = []
        # prefix = ""
        # for ch in searchWord:
        #     prefix += ch
        #     # find all starting with prefix
        #     suggestions = [p for p in products if p.startswith(prefix)]
        #     res.append(suggestions[:3])
        # return res

        # simple trie variant
        products.sort()  # ensures lexicographic order
        root = TrieNode()

        # Build the Trie
        for word in products:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                # only keep 3 smallest
                if len(node.suggestions) < 3:
                    node.suggestions.append(word)

        # Search suggestions for each prefix
        res = []
        node = root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                res.append(node.suggestions)
            else:
                node = None
                res.append([])  # prefix not found
        return res

    @pytest.mark.parametrize("products, searchWord, expected", [
        (["mobile", "mouse", "moneypot", "monitor", "mousepad"],
         "mouse",
         [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"],
          ["mouse", "mousepad"], ["mouse", "mousepad"]]
         ),
        (["havana"],
         "havana",
         [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
         ),
    ])
    def test_search_suggestion_system(self, products, searchWord, expected):
        assert self.search_suggestion_system(products, searchWord) == expected
