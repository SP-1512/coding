class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ll = s.split()
        out = ""
        for i in range(0, k):
            if i < k-1:
                out = out + ll[i] + " "
            else:
                out = out + ll[i]
        return out