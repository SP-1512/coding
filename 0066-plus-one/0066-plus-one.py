class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        out = ""
        for i in digits:
            out = out + str(i)
        
        out = int(out) + 1
        out = str(out)
        ll = []
        for i in out:
            ll.append(int(i))
        return ll

