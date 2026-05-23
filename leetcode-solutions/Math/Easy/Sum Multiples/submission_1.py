# Problem: Sum Multiples
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        for i in range(3,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                s+=i
        return s
