class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        s = 0
        ds = 0
        for i in nums:
            s += i
            while(i != 0):
                ds += i%10
                i = i//10
        return abs(s-ds)