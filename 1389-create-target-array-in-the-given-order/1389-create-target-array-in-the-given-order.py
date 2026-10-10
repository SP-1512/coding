class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        n = len(nums)
        target = []
        for i in range(n):
            target.insert(index[i], nums[i])

        return target