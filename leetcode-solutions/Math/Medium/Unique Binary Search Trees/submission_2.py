# Problem: Unique Binary Search Trees
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        num=math.factorial(2*n)
        den=(math.factorial(n+1))*(math.factorial(n))
        return num//den
