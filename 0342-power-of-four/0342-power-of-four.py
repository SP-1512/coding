class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n<=0 or n == 2 or n==3:
            return False
        else:
            while(n>=4):
                if n%4 != 0:
                    return False
                n = n // 4
        return n == 1 