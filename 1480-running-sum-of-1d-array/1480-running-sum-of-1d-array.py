class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ll = [0]*(n)
        for i in range(0,n):
            for j in range(0,i+1):
                ll[i] += nums[j]
        return ll