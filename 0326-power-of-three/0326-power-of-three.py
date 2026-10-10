class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n<=0 or n == 2:
            return False
        else:
            while(n>=3):
                if n%3 != 0:
                    return False
                n = n // 3
        return n == 1 