class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
       return sum(g for g, h in Counter(nums).items() if h == 1) 