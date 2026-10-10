class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pc = 0
        nc = 0
        for i in nums:
            if i>0:
                pc += 1
            elif i<0:
                nc += 1
        
        return max(pc, nc)
        