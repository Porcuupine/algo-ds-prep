class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
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