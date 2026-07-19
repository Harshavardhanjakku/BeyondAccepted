# Problem: Find Indices of Stable Mountains
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """ 
        return [i+1 for i in range(len(height)-1) if height[i]>threshold ]

