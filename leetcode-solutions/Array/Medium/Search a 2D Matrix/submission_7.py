# Problem: Search a 2D Matrix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 7

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            for j in i:
                if j==target:
                    return True 
        return False
                       

