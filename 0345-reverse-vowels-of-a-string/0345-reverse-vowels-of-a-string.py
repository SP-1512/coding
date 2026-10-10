class Solution:
    def reverseVowels(self, s: str) -> str:
        v = "aeiouAEIOU"
        x = list(s)
        i = 0
        j = len(s)-1
        while i < j:
            if x[i] not in v:
                i+=1
            elif x[j] not in v:
                j-=1
            else:
                x[i],x[j] = x[j],x[i]
                i += 1
                j -= 1
        return "".join(x)
