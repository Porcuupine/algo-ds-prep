import pytest


class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    """
    Hint
    A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
    Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
    For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
    Return the head of the copied linked list.
    The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
    Your code will only be given the head of the original linked list.
    Example 1:
    Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Example 2:
    Input: head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]
    Example 3:
    Input: head = [[3,null],[3,0],[3,null]]
    Output: [[3,null],[3,0],[3,null]]
    Constraints:
    0 <= n <= 1000
    -104 <= Node.val <= 104
    Node.random is null or is pointing to some node in the linked list.
    """

    def copy_random_list(self, head: ListNode | None) -> ListNode:
        if not head:
            return None

        old_to_new = {}

        # 1️⃣ Create all nodes
        curr = head
        while curr:
            old_to_new[curr] = ListNode(curr.val)
            curr = curr.next

        # 2️⃣ Connect next and random
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]


def build_random_list(values):
    """
    values: list of tuples (val, random_index or None)
    """
    if not values:
        return None

    nodes = [ListNode(v) for v, _ in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i, (_, rand_i) in enumerate(values):
        if rand_i is not None:
            nodes[i].random = nodes[rand_i]

    return nodes[0]


def serialize(head: ListNode):
    nodes = []
    idx_map = {}

    curr = head
    i = 0
    while curr:
        idx_map[curr] = i
        nodes.append(curr)
        curr = curr.next
        i += 1

    result = []
    for node in nodes:
        rand_index = idx_map[node.random] if node.random else None
        result.append([node.val, rand_index])

    return result


@pytest.mark.parametrize("values, expected", [
    ([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]], [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
    ([[1, 1], [2, 1]], [[1, 1], [2, 1]]),
    ([[3, None], [3, 0], [3, None]], [[3, None], [3, 0], [3, None]]),

])
def test_copy_list(values, expected):
    head = build_random_list(values)
    copied = Solution().copy_random_list(head)

    assert serialize(copied) == values
