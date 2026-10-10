class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        out = ""
        for i in s:
            if i.isalnum():
                out = out + i
        return out == out[::-1]