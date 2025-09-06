import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestLongestZigZagPathInABinaryTree:
    """
    You are given the root of a binary tree.
    A ZigZag path for a binary tree is defined as follow:
    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
    Change the direction from right to left or from left to right.
    Repeat the second and third steps until you can't move in the tree.
    Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
    Return the longest ZigZag path contained in that tree.

    Example 1:
    Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
    Output: 3
    Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
    Example 2:
    Input: root = [1,1,1,null,1,null,null,1,1,null,1]
    Output: 4
    Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
    Example 3:
    Input: root = [1]
    Output: 0
    Constraints:
    The number of nodes in the tree is in the range [1, 5 * 104].
    1 <= Node.val <= 100
    """

    def longest_zig_zag(self, root: TreeNode | None) -> int:
        self.max_len = 0

        def dfs(node: TreeNode | None, direction: int, length: int) -> None:
            if not node:
                return

            # update max
            self.max_len = max(self.max_len, length)

            if direction == 0:  # last move was left, so go right next
                dfs(node.right, 1, length + 1)
                dfs(node.left, 0, 1)  # reset if continue same dir
            else:
                dfs(node.left, 0, length + 1)
                dfs(node.right, 1, 1)

        dfs(root.left, 0, 1)  # start going left
        dfs(root.right, 1, 1)  # start going right

        return self.max_len


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Build binary ree from level-order list (like LeetCode input)."""
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = nodes.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


@pytest.mark.parametrize("tree_list, expected", [
    ([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1], 3),
    ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4),
])
def test_longest_zigzag(tree_list, expected):
    root = build_tree(tree_list)
    sol = TestLongestZigZagPathInABinaryTree()
    assert sol.longest_zig_zag(root) == expected
