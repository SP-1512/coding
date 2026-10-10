class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        for i in range(0,n):
            for j in range(0,n):
                if i == j and grid[i][j] == 0:
                    return False
                elif i+j == n-1 and grid[i][j] == 0:
                    return False
                elif (i!=j and i+j!=n-1) and grid[i][j] != 0:
                    return False
        return True
