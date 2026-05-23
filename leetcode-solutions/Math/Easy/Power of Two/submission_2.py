# Problem: Power of Two
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0:
            return False
        c=0
        while n :
            c+=1
            n=n&(n-1)
        return c==1
        
