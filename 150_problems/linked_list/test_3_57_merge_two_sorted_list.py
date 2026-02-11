import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(nums: list[int]) -> ListNode:
    dummy = ListNode(0)
    curr = dummy

    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next

    return dummy.next


def linked_list_to_array(head: ListNode) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    """
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
    Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    Example 2:
    Input: list1 = [], list2 = []
    Output: []
    Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
    Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
    """

    def merge_two_sorted_lists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next


@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0]),
])
def test_merge_two_sorted_list(list1, list2, expected):
    head1 = build_linked_list(list1)
    head2 = build_linked_list(list2)
    result = Solution().merge_two_sorted_lists(head1, head2)
    assert linked_list_to_array(result) == expected
