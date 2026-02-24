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


def linked_list_to_list(head: ListNode | None) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result


class Solution:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    Example 2:
    Input: head = [1], n = 1
    Output: []
    Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
    Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
    """

    def remove_nth_node(self, head: ListNode | None, n: int) -> ListNode:
        return ListNode()


@pytest.mark.parametrize("arr, n, expected", [
    # ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1], 1, [0]),
    # ([1, 2], 1, [1]),
])
def test_remove_nth_node(arr, n, expected):
    head = build_linked_list(arr)
    result = Solution().remove_nth_node(head, n)
    assert linked_list_to_list(result) == expected
