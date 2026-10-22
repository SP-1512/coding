class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        #ans = 1
        ss = "".join(sorted(s))
        l = len(s)
        return int(ss[l-1])*int(ss[l-2])