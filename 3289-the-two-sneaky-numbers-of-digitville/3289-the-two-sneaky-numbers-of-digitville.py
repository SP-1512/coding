class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        ll = []
        for i,j in freq.items():
            if j == 2:
                ll.append(i)
        return ll