class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = 0
        for i in range(0,len(s)-2):
            ll = []
            ll.append(s[i])
            ll.append(s[i+1])
            ll.append(s[i+2])
            ss = set(ll)
            if len(ss) == 3:
                c += 1
        return c


