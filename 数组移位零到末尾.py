class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums) - 1, -1, -1):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)