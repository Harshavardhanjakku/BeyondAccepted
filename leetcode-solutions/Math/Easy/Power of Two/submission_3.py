# Problem: Power of Two
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 3

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
            if (n&1)==1:
                c+=1
            n>>=1
        return c==1
        
