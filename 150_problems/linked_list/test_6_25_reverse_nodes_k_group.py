import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(arr: list[int]) -> ListNode:
    dummy = ListNode()
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_array(head: ListNode | None) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    """
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
    k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
    You may not alter the values in the list's nodes, only nodes themselves may be changed.
    Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
    Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000
    """

    def reverse_nodes(self, head: ListNode | None, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        while True:
            # find kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # less than k nodes left

            group_next = kth.next

            # reverse k nodes
            prev, curr = group_next, group_prev.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # reconnect
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp


@pytest.mark.parametrize("arr, k, expected", [
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
])
def test_reverse_nodes(arr, k, expected):
    head = build_linked_list(arr)
    result = Solution().reverse_nodes(head, k)
    assert linked_list_to_array(result) == expected
