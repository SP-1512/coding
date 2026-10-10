class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ll = []
        for i in range(0,n):
            count = 0
            for j in range(0,n):
                if nums[j] < nums[i]:
                    count += 1
            ll.append(count)
    
        return ll

            