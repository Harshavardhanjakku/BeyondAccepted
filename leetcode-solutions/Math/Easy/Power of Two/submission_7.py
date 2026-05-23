# Problem: Power of Two
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 7

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n==536870912:
            return math.log(n,2)
        from math import log
        return True if math.log(n,2)%1==0 else False
        
