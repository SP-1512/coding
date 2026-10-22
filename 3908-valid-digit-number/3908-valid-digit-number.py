class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n = str(n)
        if n[0] == str(x):
            return False
        elif str(x) in n:
            return True
        else:
            return False