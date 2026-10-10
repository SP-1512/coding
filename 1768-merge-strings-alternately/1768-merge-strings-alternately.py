class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        minn = min(n,m)
        out = ""
        for i in range(0,minn):
            out += word1[i] + word2[i]
        if m > n:
            for i in range(minn,max(n,m)):
                out += word2[i]
        elif n > m:
            for i in range(minn,max(n,m)):
                out += word1[i]
        return out