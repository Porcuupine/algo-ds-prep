class TestMoveZeroes:
    """Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Example 2:
    Input: nums = [0]
    Output: [0]
    Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
    """

    def move_zeroes(self, nums: list[int]) -> None:
        """
        [0,1,0,3,12]
         s f     change and f++, s++
        [1,0,0,3,12]
           s f   f++ ? nums[s] != 0 ? s++: ;
           s   f    change
        [1,3,0,0,12]
           s   f      f++   nums[s] != 0 ? s++ : ;
             s    f   change
        [1,3,12,0,0]
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

            fast += 1
            if nums[slow] != 0:
                slow += 1

    def test_move_zeroes(self):
        nums = [0, 1, 0, 3, 12]
        self.move_zeroes(nums)
        assert nums == [1, 3, 12, 0, 0]
