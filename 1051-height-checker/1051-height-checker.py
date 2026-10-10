class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = 0
        exp = sorted(heights)
        for i in range(0, len(heights)):
            if heights[i] != exp[i]:
                count += 1
        return count