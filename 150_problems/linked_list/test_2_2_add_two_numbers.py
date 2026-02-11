class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
    Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]
    Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
    Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
    """

    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


def build_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


import pytest


class Test_AddTwoNumbers:
    @pytest.mark.parametrize(
        "l1, l2, expected",
        [
            ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
            ([0], [0], [0]),
            ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ],
    )
    def test_add_two_numbers(self, l1, l2, expected):
        head1 = build_list(l1)
        head2 = build_list(l2)
        result = Solution().addTwoNumbers(head1, head2)
        assert list_to_array(result) == expected
