# Problem: Search a 2D Matrix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 6

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if i[-1]<target:
                continue
            else:
                for j in i:
                    if j==target:
                        return True
                return False
        return False
                       

