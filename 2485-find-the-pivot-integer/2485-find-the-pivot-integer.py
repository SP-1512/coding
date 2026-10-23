class Solution:
    def pivotInteger(self, n: int) -> int:
        ls = 0
        rs = int((n*(n+1))/2)
        n += 1
        for i in range(1, n):
            ls += i
            if ls == rs:
                return i
            rs -= i
        return -1
