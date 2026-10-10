class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ll = []

        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        if len(nums) == k:
            return nums
        
        for i in range(0,k):
            ll.append(int(count[i][0]))

        return ll
