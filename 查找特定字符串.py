class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for index in arr:
            if arr.count(index) == 1:
                k -= 1
            if k == 0:
                return index
        if k > 0:
            return ""