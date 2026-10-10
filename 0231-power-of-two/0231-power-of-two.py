class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n<=0:
            return False
        else:
            temp = n
            while(temp>=2):
                if temp%2 != 0:
                    return False
                temp = temp // 2

        return True
