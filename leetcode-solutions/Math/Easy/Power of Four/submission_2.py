# Problem: Power of Four
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        import math
        if n<=0:
            return False
        return True if math.log(n,4)%1==0 else False
