class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        ll = []
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for i, j in freq.items():
            if j>1:
                ll.append(i)
        for i in range(1, len(nums)+1):
            if i not in freq.keys():
                ll.append(i)
        return ll
        