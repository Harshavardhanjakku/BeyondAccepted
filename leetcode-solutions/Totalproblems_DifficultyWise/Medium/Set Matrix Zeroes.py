# Set Matrix Zeroes
# Difficulty: Medium
# Language: python

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row={}
        col={}
        m=len(matrix)
        n=len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:
                    row[r]=True
                    col[c]=True
        for i in range(m):
            for j in range(n):
                if i in row or j in col :
                    matrix[i][j]=0
        return matrix

