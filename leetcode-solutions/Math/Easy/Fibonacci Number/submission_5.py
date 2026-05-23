# Problem: Fibonacci Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 5

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b=0,1
        s=0
        if n==0:
            return a
        elif n==1:
            return b
        for i in range(2,n+1):
            s=a+b
            a=b
            b=s
        return s
                


