# Problem: Power of Four
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        import math
        return True if n>0 and math.log(n,4)%1==0 else False
