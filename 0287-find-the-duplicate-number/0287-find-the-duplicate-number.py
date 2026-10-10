class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                return i