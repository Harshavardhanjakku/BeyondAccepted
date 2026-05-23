# Problem: Smallest Number With All Set Bits
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 4

class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n:
            if n&(n+1)==0:
                return  n 
            n=n+1
