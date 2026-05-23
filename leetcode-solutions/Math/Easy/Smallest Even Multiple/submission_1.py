# Problem: Smallest Even Multiple
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n%2==0 else n*2
        
