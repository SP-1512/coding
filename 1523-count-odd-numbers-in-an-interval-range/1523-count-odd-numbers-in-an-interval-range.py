class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low)%2 == 0:
            count = (high - low)/2
            if high%2 != 0 or low%2 != 0: count +=1
        else:
            count = ((high - low)/2) + 1
        return int(count)