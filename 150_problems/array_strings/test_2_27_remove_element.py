import pytest


class TestRemoveElement:
    """
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
    Custom Judge:
    The judge will test your solution with the following code:
    int[] nums = [...]; // Input array
    int val = ...; // Value to remove
    int[] expectedNums = [...]; // The expected answer with correct length.
                                // It is sorted with no values equaling val.
    int k = removeElement(nums, val); // Calls your implementation
    assert k == expectedNums.length;
    sort(nums, 0, k); // Sort the first k elements of nums
    for (int i = 0; i < actualLength; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.
    Example 1:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    Example 2:
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    Constraints:
    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100    """

    def remove_element(self, nums: list[int], val: int) -> int:
        if not nums: return 0
        k = 0
        c = 0
        index1 = index2 = 0
        # iterate through loop
        while index1 < len(nums):
            # value is not found, increment index by 1
            if nums[index1] != val:
                index1 += 1
                k += 1
                continue
            # value is not found
            c += 1  # keep track of vals found
            index2 = index1 + 1
            # find all subsequent vals
            while nums[index2] == val:
                c += 1
                index2 += 1
            # if index2 did not reach the end, swap with the current c
            if index2 >= len(nums):
                temp = 0
                # swap c times
            if nums[index2] != val:
                nums[index1], nums[index2] = nums[index2], nums[index1]
                index1 += 1
                index2 += 1
            else:
                index2 += 1
            if index2 == len(nums) - 1:
                return index1 - 1
            index1 += 1
        return k

    @pytest.mark.parametrize("nums, val, expected", [
        ([3, 2, 2, 3], 3, 2),
    ])
    def test_remove_element(self, nums, val, expected):
        assert self.remove_element(nums, val) == expected
