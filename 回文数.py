class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        if str1[0:] ==  str1[::-1]:
            return True
        else:
            return False