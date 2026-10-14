class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n%2 == 0:
            return (n//2)*2 - 1
        elif n==1:
            return 0
        else:
            return (n) - 1