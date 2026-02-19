import pytest


class ListNode:
    def __init__(self, val=0, next=next):
        self.val = val
        self.next = next


def build_linked_list(nums: list[int]):
    dummy = ListNode()
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy


def linked_list_to_list(head: ListNode | None):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    """Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
    Example 1:
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
    Example 2:
    Input: head = [5], left = 1, right = 1
    Output: [5]
    Constraints:
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n
    Follow up: Could you do it in one pass?"""

    def reverse_linked_list(self, head: ListNode | None, left: int, right: int):
        while left < right:
            head[left], head[right] = head[right], head[left]

            left += 1
            right -= 1

        return head




@pytest.mark.parametrize("values, left, right, expected", [
    ([1, 2, 3, 4, 5], 2, 4),
    ([5], 1, 1),
])
def test_reverse_linked_list(values, left, right, expected):
    head = build_linked_list(values)
    result = Solution().reverse_linked_list(head)
    assert linked_list_to_list(result) == expected
