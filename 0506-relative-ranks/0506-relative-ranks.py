class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        l = sorted(score)[::-1]
        z = 1
        for i in l:
            x = score.index(i)
            if z == 1:
                score[x] = "Gold Medal"
            elif z == 2:
                score[x] = "Silver Medal"
            elif z == 3:
                score[x] = "Bronze Medal"
            else:
                score[x] = str(z)
            z += 1
        return score