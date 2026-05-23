# Problem: Fibonacci Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 7

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(n):
            if n==0 or n==1:
                return n
            else:
                return f(n-1)+f(n-2)
        return f(n)   
