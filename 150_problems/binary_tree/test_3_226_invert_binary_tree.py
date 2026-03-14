from collections import deque

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def built_tree(values: list[int | None]):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
        return root


def tree_list_to_list(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


class TestInvertBinaryTree:
    """
    Given the root of a binary tree, invert the tree, and return its root.
    Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]
    Example 3:
    Input: root = []
    Output: []
    Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
    """

    def invert_binary_tree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        return root

    @pytest.mark.parametrize("values, expected", [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        # ([2, 1, 3], [2, 3, 1]),
        # ([], []),
    ])
    def test_invert_binary_tree(self, values, expected):
        root = built_tree(values)
        result = self.invert_binary_tree(root)
        assert tree_list_to_list(result) == expected
