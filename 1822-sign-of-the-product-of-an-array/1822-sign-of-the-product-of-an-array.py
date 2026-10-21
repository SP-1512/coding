class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if 0 in nums:
            return 0
        ans = 1
        for i in nums:
            ans *= i
        if ans > 0:
            return 1
        else:
            return -1