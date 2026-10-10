class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ll = []
        top = 0
        left = 0
        bottom = len(matrix)
        right = len(matrix[0])
        while top < bottom and left < right:
            for i in range(left,right):
                ll.append(matrix[top][i])
            top += 1
            for i in range(top,bottom):
                ll.append(matrix[i][right-1])
            right -= 1

            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    ll.append(matrix[bottom-1][i])
            bottom -= 1
            
            if left < right:
                for i in range(bottom-1,top-1,-1):
                    ll.append(matrix[i][left])
            left += 1
        return ll                