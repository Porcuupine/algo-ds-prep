import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr: list[int]):
    if not arr:
        return None
    nodes = [None if v is None else TreeNode(v) for v in arr]
    for i in range(len(arr)):
        if nodes[i] is not None:
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(arr):
                nodes[i].left = nodes[left]

            if right < len(arr):
                nodes[i].right = nodes[right]
    return nodes[0]


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

    def max_depth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        return 1 + max(left_depth, right_depth)

    @pytest.mark.parametrize("root, expected", [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ])
    def test_max_depth(self, tree, expected):
        root = build_tree(tree)
        assert self.max_depth(root) == expected
