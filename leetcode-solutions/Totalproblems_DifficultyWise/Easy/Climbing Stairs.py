# Climbing Stairs
# Difficulty: Easy
# Language: python

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return n 
        a=2
        b=3
        for i in range(3,n):
            c=a+b
            a=b
            b=c
        return c

