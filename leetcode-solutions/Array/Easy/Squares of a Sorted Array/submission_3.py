# Problem: Squares of a Sorted Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([x**2 for x in nums])
        
