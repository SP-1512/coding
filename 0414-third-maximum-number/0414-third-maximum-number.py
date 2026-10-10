class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        out = []
        for i in nums:
            if i not in out:
                out.append(i)
        out.sort(reverse=True)
        if len(out) >= 3:
            return out[2]
        else:
            return out[0]