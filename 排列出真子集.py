class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list1 = [[]]
        nums.sort()
        for i in range(len(nums)):
            for j in range(len(list1)):
                if list1[j] + [nums[i]] not in list1:
                    list1.append(list1[j] + [nums[i]])


        return list1