class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i]+nums[j] == target and i not in ans and j not in ans:
                        ans.append(i)
                        ans.append(j)
        
        return sorted(ans)

        