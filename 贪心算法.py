class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left = 0
        right = 0
        for index in range(len(colors)):
            if colors[index] != colors[0]:
                left = index
        colors = colors[::-1]
        for index2 in range(1, len(colors)):
            if colors[index2] != colors[0]:
                right = index2
        return max(left, right)
        