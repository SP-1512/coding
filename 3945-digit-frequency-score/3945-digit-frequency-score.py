class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = {}
        s = str(n)
        ans = 0
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        
        for i,j in freq.items():
            ans += int(i)*j
        return ans