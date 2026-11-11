class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i],matrix[i]
            
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r],matrix[r][c]
        


        