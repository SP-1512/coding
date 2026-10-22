class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ma = max(nums)
        mi = min(nums)
        ans = []
        for i in range(mi, ma):
            if i not in nums:
                ans.append(i)
        return ans