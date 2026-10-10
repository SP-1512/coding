class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max = 0
        count = 0
        for i in nums:
            if i == 0:
                if count > max:
                    max = count
                count = 0
            else:
                count += 1
        if count > max:    
            max = count
        return max 