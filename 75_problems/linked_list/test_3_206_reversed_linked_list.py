import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TestReversedLinkedList:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    Example 1:

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    Example 2:
    Input: head = [1,2]
    Output: [2,1]
    Example 3:
    Input: head = []
    Output: []

    Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
    """

    def reverseList(self, head: "ListNode") -> "ListNode":
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def build_linked_list(self, values: list[int]) -> "ListNode":
        if not values:
            return None
        head = ListNode(values[0])
        curr = head
        for v in values[1:]:
            curr.next = ListNode(v)
            curr = curr.next
        return head

    def linked_list_to_list(self, head: "ListNode") -> list[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    @pytest.mark.parametrize("inp, expected", [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ])
    def test_reverse_list(self, inp, expected):
        head = self.build_linked_list(inp)
        new_head = self.reverseList(head)
        assert self.linked_list_to_list(new_head) == expected
