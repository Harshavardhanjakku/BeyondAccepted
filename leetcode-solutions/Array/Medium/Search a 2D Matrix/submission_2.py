# Problem: Search a 2D Matrix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def findrow(matrix,target):
            row=0
            for i in matrix:
                if target<=i[-1]:
                    return row
                row+=1
            return -1
        def findcolumn(matrix,target,row):
            for i in matrix[row]:
                if target==i:
                    return True
            return False
        myrow=findrow(matrix,target)
        return findcolumn(matrix,target,myrow)

