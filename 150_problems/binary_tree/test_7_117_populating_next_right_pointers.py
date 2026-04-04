import pytest


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    Given a binary tree
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
    Initially, all next pointers are set to NULL.
    Example 1:
    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]
    Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
    Example 2:
    Input: root = []
    Output: []
    Constraints:
    The number of nodes in the tree is in the range [0, 6000].
    -100 <= Node.val <= 100
    Follow-up:
    You may only use constant extra space.
    The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
    """

    def populate(self, root: Node | None) -> Node | None:
        if not root:
            return None

        current = root
        while current:
            dummy = Node(0)
            tail = dummy

            # iterate current level
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next

            current = dummy.next

        return root


def build_tree(values):
    if not values:
        return None

    nodes = [None if v is None else Node(v) for v in values]

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


def tree_levels_with_root(root: Node):
    """Return list of lists of node values at each level using .next pointers"""
    result = []
    while root:
        level = []
        current = root
        next_level_start = None

        while current:
            level.append(current.val)
            if not next_level_start:
                next_level_start = current.left or current.right
            current = current.next

        result.append(level)
        root = next_level_start

    return result


@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5, None, 7], [[1], [2, 3], [4, 5, 7]]),
    ([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]]),
    ([], []),
    ([1], [[1]]),
])
def test_populate(values, expected):
    root = build_tree(values)
    Solution().populate(root)
    assert tree_levels_with_root(root) == expected
