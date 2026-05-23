# Problem: Search a 2D Matrix II
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 4

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

