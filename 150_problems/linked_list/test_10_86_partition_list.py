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


def linked_list_to_list(head: ListNode) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    """
    Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
    You should preserve the original relative order of the nodes in each of the two partitions.
    Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
    Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]
    Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
    """

    def partition(self, head: ListNode, x: int):
        before_head = ListNode()
        after_head = ListNode()
        before = before_head
        after = after_head

        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next

        after.next = None
        before.next = after_head.next
        return before_head.next


@pytest.mark.parametrize("arr, x, expected", [
    ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
    ([2, 1], 2, [1, 2]),
])
def test_partition(arr, x, expected):
    head = build_linked_list(arr)
    result = Solution().partition(head, x)
    assert linked_list_to_list(result) == expected
