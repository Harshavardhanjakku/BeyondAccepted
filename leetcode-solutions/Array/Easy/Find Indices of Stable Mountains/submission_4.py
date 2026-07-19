# Problem: Find Indices of Stable Mountains
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        n=len(height)
        res=[]
        for i in range(n-1):
            if height[i]>threshold:
                res.append(i+1)
        return res

