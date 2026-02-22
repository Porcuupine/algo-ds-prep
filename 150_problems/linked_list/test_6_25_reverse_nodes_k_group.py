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
        dummy_head = ListNode()
        dummy_head.next = head

        prev_group_tail = dummy_head

        while True:
            # find the end of the current k-group
            group_end = prev_group_tail
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy_head.next  # not enough nodes left

            next_group_head = group_end.next

            # reverse this group
            node = prev_group_tail.next  # first node in group
            reversed_head = next_group_head  # this will become the tail connector

            for _ in range(k):
                next_node = node.next
                node.next = reversed_head
                reversed_head = node
                node = next_node

            # reconnect previous group to the reversed one
            new_group_tail = prev_group_tail.next  # will become tail after reverse
            prev_group_tail.next = reversed_head  # connect previous group to new head
            prev_group_tail = new_group_tail  # move to next group


@pytest.mark.parametrize("arr, k, expected", [
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
])
def test_reverse_nodes(arr, k, expected):
    head = build_linked_list(arr)
    result = Solution().reverse_nodes(head, k)
    assert linked_list_to_array(result) == expected
