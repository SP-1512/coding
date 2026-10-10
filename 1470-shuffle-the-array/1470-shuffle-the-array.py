class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ll = []
        for i in range(0,n):
            ll.append(nums[i])
            ll.append(nums[n+i])
        return ll