# Smallest Even Multiple
# Difficulty: Easy
# Language: python

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n%2==0 else n*2
        
