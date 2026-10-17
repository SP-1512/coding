class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        while len(nums) != 0:
            m = min(nums)
            nums.remove(m)
            n = min(nums)
            nums.remove(n)
            ans.append(n)
            ans.append(m)
        return ans
