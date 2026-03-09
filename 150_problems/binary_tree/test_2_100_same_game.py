import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true
    Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false
    Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false
    Constraints:
    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104
    """

    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # both nodes empty
        if not p and not q:
            return True
        # one empty
        if not p or not q:
            return False
        # values different
        if p.val != q.val:
            return False
            # check children
        return (
            self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        )


def build_tree(values):
    if not values:
        return None
    nodes = [
        None if v is None else TreeNode(v)
        for v in values
    ]
    for i in range(len(values)):
        if nodes[i] is None:
            continue

    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(values):
        nodes[i].left = nodes[left]
    if right < len(values):
        nodes[i].right = nodes[right]

    return nodes[0]


@pytest.mark.parametrize("p, q, expected")
def test_is_same_tree(p, q, expected):
    tree1 = build_tree(p)
    tree2 = build_tree(q)
    assert Solution().is_same_tree(tree1, tree2) == expected
