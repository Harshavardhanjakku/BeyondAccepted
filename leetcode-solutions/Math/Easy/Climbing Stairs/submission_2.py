# Problem: Climbing Stairs
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return n 
        a,b=1,2
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c 
        return c

