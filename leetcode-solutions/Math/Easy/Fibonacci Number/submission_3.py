# Problem: Fibonacci Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        c=1
        if n<2:
            return n
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return c

