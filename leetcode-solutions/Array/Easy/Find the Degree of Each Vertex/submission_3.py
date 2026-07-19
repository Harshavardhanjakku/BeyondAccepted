# Problem: Find the Degree of Each Vertex
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        return [ sum(row) for row in matrix]
