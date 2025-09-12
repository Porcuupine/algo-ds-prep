import queue

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[int | None]) -> TreeNode | None:
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


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    if not root:
        return []
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


class TestSearchInBinaryTree:
    """
    You are given the root of a binary search tree (BST) and an integer val.
    Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

    Example 1:
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]
    Example 2:
    Input: root = [4,2,7,1,3], val = 5
    Output: []
    Constraints:
    The number of nodes in the tree is in the range [1, 5000].
    1 <= Node.val <= 107
    root is a binary search tree.
    1 <= val <= 107 
    """

    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    @pytest.mark.parametrize(
        "tree_list, val, expected",
        ([4, 2, 7, 1, 3], 2, [2, 1, 3]),
        # ([4, 2, 7, 1, 3], 5, []),
    )
    def test_search_bst(tree_list, val, expected):
        root = build_tree(tree_list)
        sol = TestSearchInBinaryTree()
        result = sol.searchBST(root, val)
        assert tree_to_list(result) == expected
