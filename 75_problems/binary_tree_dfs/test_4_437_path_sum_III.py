from collections import defaultdict

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestPathSumIII:
    """
    Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
    The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

    Example 1:
    Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    Output: 3
    Explanation: The paths that sum to 8 are shown.
    Example 2:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: 3
    Constraints:
    The number of nodes in the tree is in the range [0, 1000].
    -109 <= Node.val <= 109
    -1000 <= targetSum <= 1000
    """

    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        self.count = 0

        def dfs(node: TreeNode | None, current_sum: int) -> None:
            if not node:
                return
            current_sum += node.val

            # count paths ending at this node
            self.count += prefix[current_sum - targetSum]

            prefix[current_sum] += 1
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            prefix[current_sum] -= 1  # backtrack

        dfs(root, 0)
        return self.count


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Build binary tree from level-order list"""
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


@pytest.mark.parametrize("tree_list, target, expected",
                         [([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
                          ([1], 1, 1), ])
def test_path_sum(tree_list, target, expected):
    root = build_tree(tree_list)
    sol = TestPathSumIII()
    assert sol.path_sum(root, target) == expected
