class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = 0
        for i, v in enumerate(nums):
            if v:
                tmp = nums[i0]
                nums[i0] = v
                nums[i] = tmp
                i0 += 1
