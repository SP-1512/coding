class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        

        for i,j in dic.items():
            if j > int(n/2):
                return i