class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        ns = str(n)
        for i in range(0,len(str(n))):
            if i%2 == 0:
                ans += int(ns[i])
            else:
                ans = ans + (-1*int(ns[i]))
        return ans