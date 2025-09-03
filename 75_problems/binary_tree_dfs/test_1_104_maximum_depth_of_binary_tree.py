# test_max_depth.py
import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestMaxDepth:
    """
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    Example 2:
    Input: root = [1,null,2]
    Output: 2
    Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
    """

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


def build_tree(values):
    """
    Build a binary tree from a list of values in level-order.
    None represents a missing node.
    """
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


@pytest.mark.parametrize("values, expected", [
    ([3, 9, 20, None, None, 15, 7], 3),  # example tree → depth 3
    ([1, None, 2], 2),  # skewed right
])
def test_max_depth(values, expected):
    root = build_tree(values)
    sol = TestMaxDepth()
    assert sol.maxDepth(root) == expected
