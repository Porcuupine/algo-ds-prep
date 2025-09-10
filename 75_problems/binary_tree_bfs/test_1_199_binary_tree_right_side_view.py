import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestBinaryTreeRightSideView:
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

    Example 1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
    Explanation:
    Example 2:
    Input: root = [1,2,3,4,null,null,null,5]
    Output: [1,3,4,5]
    Explanation:
    Example 3:
    Input: root = [1,null,3]
    Output: [1,3]
    Example 4:
    Input: root = []
    Output: []
    Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
    """

    def right_side_view(self, root: TreeNode | None) -> list[int]:
        result = []

        def dfs(node: TreeNode | None, depth: int):
            if not node:
                return
            if depth == len(result):  # first node at this depth
                result.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Build binary tree from level-order list (like LeetCode input)."""
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


@pytest.mark.parametrize(
    "tree_list,expected",
    [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, 2, 3, 4, None, None, None, None, 5], [1, 3, 5]),
    ],
)
def test_right_side_view(tree_list, expected):
    root = build_tree(tree_list)
    sol = TestBinaryTreeRightSideView()
    assert sol.right_side_view(root) == expected
