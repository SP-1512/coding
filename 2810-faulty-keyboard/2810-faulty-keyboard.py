class Solution:
    def finalString(self, s: str) -> str:
        out = ""
        for i in s:
            if i != "i":
                out = out + i
            else:
                out = out[::-1]
        return out