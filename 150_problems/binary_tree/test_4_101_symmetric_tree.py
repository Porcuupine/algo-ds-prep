from collections import deque

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[int] | None) -> TreeNode:
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
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


def tree_list_to_list(root: TreeNode | None) -> list[int] | None:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            result.append(node.left)
            result.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    def is_symmetric(self, root: TreeNode | None) -> bool:
        """
        Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
        Example 1:
        Input: root = [1,2,2,3,4,4,3]
        Output: true
        Example 2:
        Input: root = [1,2,2,null,3,null,3]
        Output: false
        Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        -100 <= Node.val <= 100
        :param root: 
        :return: 
        """

        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left)
            )

        if not root:
            return True
        return is_mirror(root.left, root.right)


@pytest.mark.parametrize("root, expected", [
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
])
def test_is_symmetric(root, expected):
    tree = build_tree(root)
    assert Solution().is_symmetric(tree) == expected
