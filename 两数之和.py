class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for index, num in enumerate(nums):
            opposite_num = target - num
            if opposite_num in dict1:
                return [dict1[opposite_num], index]
            dict1[num] = index
        return None