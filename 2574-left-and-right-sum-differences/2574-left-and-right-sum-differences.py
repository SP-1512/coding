class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls = []
        rs = []
        s = len(nums)
        for i in range(0, s):
            ans = 0
            for j in range(0, i):
                ans += nums[j]
            ls.append(ans)
        for i in range(s):
            ans = 0
            for j in range(i+1, s):
                ans += nums[j]
            rs.append(ans)
        for i in range(0, s):
            ls[i] = abs(ls[i] - rs[i])
        rs.clear()
        return ls
        
