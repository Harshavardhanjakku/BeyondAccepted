# Rotate Image
# Difficulty: Medium
# Language: python

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in range(n):
            i,j=0,n-1
            while i<j:
                matrix[row][i],matrix[row][j]=matrix[row][j],matrix[row][i]
                i+=1
                j-=1
        return matrix
