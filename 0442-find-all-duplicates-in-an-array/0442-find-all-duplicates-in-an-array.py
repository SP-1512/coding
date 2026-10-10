class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        ll = []
        count = sorted(count.items(), key=lambda x:x[1],reverse = True)
        for i,j in count:
            if j == 2:
                ll.append(int(i))
        return ll 
        