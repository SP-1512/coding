class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr1 = [0]*(2*n)
        for i in range(0,n):
            arr1[i] = nums[i]
            arr1[i+n] = nums[i] 

        return arr1