class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums = set(nums)
        ll = []
        for i in range(1, n+1):
            if i not in nums:
                ll.append(i)
        return ll
        