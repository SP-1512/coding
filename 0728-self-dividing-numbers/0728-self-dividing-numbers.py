class Solution:
    def selfDiv(self, i):
        temp = i
        while(temp != 0):
            temp1 = temp%10
            if i%temp1 != 0:
                return False
            temp //= 10
        return True
    
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for i in range(left,right+1):
            if '0' in str(i):
                continue
            else:
                if self.selfDiv(i):
                    ans.append(i)
        return ans   
                
                    
                

        