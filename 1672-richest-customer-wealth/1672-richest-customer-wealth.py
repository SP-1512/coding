class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max = 0
        for i in accounts:
            sum = 0
            for j in i:
                sum += j
            if sum > max:
                max = sum
        return max