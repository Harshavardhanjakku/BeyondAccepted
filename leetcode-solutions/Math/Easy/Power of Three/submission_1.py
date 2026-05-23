# Problem: Power of Three
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        else:
            import math
            res=math.log(n,3)
            if round(res,10)-int(res)==1 or res-int(res)==0:
                return True
            else:
                return False
