import heapq

import pytest


class TestLargestElement:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    Can you solve it without sorting?
    Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
    Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
    Constraints:
    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104
    """

    def largest_element(self, nums: list[int], k: int) -> int:

        # nums.sort(reverse=True)   # O(n log n)
        # return nums[k - 1]

        heap = []
        for num in nums:
            heapq.heappush(heap, num)  # O(log n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    @pytest.mark.parametrize("nums, k, expected", [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ])
    def test_largest_element(self, nums, k, expected):
        assert self.largest_element(nums, k) == expected
