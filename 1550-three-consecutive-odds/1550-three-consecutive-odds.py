class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        n = len(arr)-2
        for i in range(0,n):
            if arr[i]%2 == 1 and arr[i+1]%2 == 1 and arr[i+2]%2 == 1:
                return True
        return False