class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        sum = 0
        for i in range(0,n):
            for j in range(0,n):
                if i == j:
                    sum+=mat[i][j]
                elif i+j == n-1:
                    sum+=mat[i][j]
        return sum