# Problem: N-th Tribonacci Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return n
        a,b,c=0,1,1
        for _ in range(3,n+1):
            a,b,c=b,c,a+b+c
        return c
        
