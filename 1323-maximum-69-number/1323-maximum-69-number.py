class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        out = ""
        flag = True
        for i in range(0,len(s)):
            if s[i] == '6' and flag:
                out = out + '9'
                flag = False
            else:
                out = out + s[i]
        
        out = int(out)
        return out