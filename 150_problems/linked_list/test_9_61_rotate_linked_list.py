from tokenize import Special

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(arr: list[int]):
    dummy = ListNode()
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: ListNode) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    """
    Given the head of a linked list, rotate the list to the right by k places.
    Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
    Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]
    Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109
    """

    def rotate_linked_list(self, head: ListNode, k: int) -> ListNode:
        # 1. find length and last node:
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. reduce k:
        k %= length
        if k == 0:
            return head

        # 3. make circular
        tail.next = head

        # 4. find new tail (length - k - 1 steps)
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # 5. break circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head


@pytest.mark.parametrize("arr, k, expected", [
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([0, 1, 2], 4, [2, 0, 1]),
])
def test_rotate_linked_list(arr, k, expected):
    head = build_linked_list(arr)
    result = Solution().rotate_linked_list(head, k)
    assert linked_list_to_list(result) == expected
