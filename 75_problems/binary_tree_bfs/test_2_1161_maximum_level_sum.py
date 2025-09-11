from collections import deque

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[int | None]):
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


class TestMaximumLevelSum:
    """
    Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
    Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
    Example 1:
    Input: root = [1,7,0,7,-8,null,null]
    Output: 2
    Explanation:
    Level 1 sum = 1.
    Level 2 sum = 7 + 0 = 7.
    Level 3 sum = 7 + -8 = -1.
    So we return the level with the maximum sum which is level 2.
    Example 2:
    Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
    Output: 2
    Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -105 <= Node.val <= 105
    """

    def maximum_level_sum(self, root: list[int | None]) -> int:
        if not root:
            return 0

        queue = deque([root])
        max_sum = float("-inf")
        max_level = 1
        level = 1

        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1

        return max_level

    @pytest.mark.parametrize("tree_list, expected", [
        ([1, 7, 0, 7, -8, None, None], 2),
        ([989, None, 10250, 98693, -89388, None, None, None, -32127], 2),
    ])
    def test_maximum_level_sum(self, tree_list, expected):
        root = build_tree(tree_list)
        assert self.maximum_level_sum(root) == expected
