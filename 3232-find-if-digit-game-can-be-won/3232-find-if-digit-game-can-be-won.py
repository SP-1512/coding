class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a = 0
        b = 0
#        sc = 0
#        dc = 0
        for i in nums:
            if i >9:
                b += i
#                dc += 1
            else:
                a += i
#                sc += 1
        return a!=b
        