class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        ans = 0
        for i, j in count.items():
            if j == 1:
                ans += int(i)
        
        return ans