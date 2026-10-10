class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        out = ""
        out1 = ""
        for i in word1:
            out = out + i
        for j in word2:
            out1 = out1 + j
        return out == out1