import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestLeafSimilarTrees:
    """
    Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
    For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
    Two binary trees are considered leaf-similar if their leaf value sequence is the same.
    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

    Example 1:
    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    Output: true
    Example 2:
    Input: root1 = [1,2,3], root2 = [1,3,2]
    Output: false
    Constraints:
    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].
    """

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)

        return dfs(root1) == dfs(root2)


def build_tree(values):
    """Build a binary tree from level-order values (None = missing)."""
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


@pytest.mark.parametrize("tree1, tree2, expected", [
    ([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
     [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8], True),
])
def test_leaf_similar(tree1, tree2, expected):
    root1 = build_tree(tree1)
    root2 = build_tree(tree2)
    sol = TestLeafSimilarTrees()
    assert sol.leafSimilar(root1, root2) == expected
