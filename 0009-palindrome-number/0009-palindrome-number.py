class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        if x < 0:
            return False
        if n == n[::-1]:
            return True
        else:
            return False
        