class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = []
        for i in candies:
            if i+extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans

        