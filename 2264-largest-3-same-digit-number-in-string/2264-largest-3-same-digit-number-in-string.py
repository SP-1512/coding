class Solution:
    def largestGoodInteger(self, num: str) -> str:
        great = 0
        zero = False

        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                if num[i] == "0":
                    zero = True
                n = int(num[i])
                if great <= n:
                    great = n
        if zero:
            return str(great)*3
        else:
            if great == 0:
                return ""
            
            return str(great)*3