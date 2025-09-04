import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a binary tree from level-order values (None = missing)."""
    if not values:
        return None
    # 1. Create TreeNode objects (or None)
    nodes = [TreeNode(v) if v is not None else None for v in values]

    # 2. Reverse list so we can pop from the end efficiently
    kids = nodes[::-1]

    # 3. First element is the root
    root = kids.pop()

    # 4. Assign children left/right
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


class TestCountGoodNodesInBinaryTree:
    """
    Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
    Return the number of good nodes in the binary tree.

    Example 1:
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.
    Example 2:
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
    Example 3:
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.
    Constraints:
    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4].
    """

    def count_good_nodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)
            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

        return dfs(root, root.val)

    @pytest.mark.parametrize("tree, expected", [
        ([3, 1, 4, 3, None, 1, 5], 4),
        ([3, 3, None, 4, 2], 3),
        ([1], 1),
    ])
    def test_count_good_nodes(self, tree, expected):
        root = build_tree(tree)
        sol = TestCountGoodNodesInBinaryTree()
        assert sol.count_good_nodes(root) == expected
