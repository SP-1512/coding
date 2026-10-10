class Solution:
    def reverseDegree(self, s: str) -> int:
        rev = 0
        for i in range(0,len(s)):
            rev += (ord("z")+1 - ord(s[i])) * (i+1)
        return rev