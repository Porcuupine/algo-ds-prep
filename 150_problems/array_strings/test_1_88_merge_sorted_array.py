import pytest


class TestMergeSortedArray:
    """88. Merge Sorted Array
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

    Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].

    Example 3:
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

    Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109
    """

    def merge_sorted_array(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # if not n:
        #     return
        # if not m:
        #     for i in range(len(nums1)):
        #         nums1[i] = nums2[i]
        #     return
        #
        # index1 = index2 = 0
        # while index1 < len(nums1):
        #     if index1 >= m:
        #         nums1[index1] = nums2[index2]
        #         index1 += 1
        #         index2 += 1
        #
        #     elif nums1[index1] <= nums2[index2]:
        #         index1 += 1
        #     else:
        #         nums1[index1], nums2[index2] = nums2[index2], nums1[index1]
        #         index1 += 1
        #
        #
        #
        # return None
        # case 2
        if not n:
            return
        # case 3
        if not m:
            # copy each num from nums2 to nums1
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
            return

        # case 1
        index1, index2 = 0, 0

        while index1 < len(nums1):
            current_element1, current_element2 = nums1[index1], nums2[index2]
            # add remaining from nums2 if nums1 is at the end
            if index1 >= m:
                nums1[index1] = current_element2
                index1 += 1
                index2 += 1
            elif current_element1 <= current_element2:  # element1 is lesser
                index1 += 1
            else:  # if element2 is lesser
                # swap element1 with element2
                nums1[index1] = current_element2
                nums2[index2] = current_element1
                index1 += 1

    @pytest.mark.parametrize(
        'nums1, nums2, m, n, expected', [
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ]
    )
    def test_merge_sorted_array(self, nums1, m, nums2, n, expected):
        self.merge_sorted_array(nums1, m, nums2, n)
        assert nums1 == expected
