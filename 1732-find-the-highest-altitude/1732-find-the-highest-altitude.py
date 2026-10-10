class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max = 0
        for i in range(0,len(gain)):
            count = 0
            for j in range(0,i+1):
                count += gain[j]
            if max < count:
                max = count
        
        return max