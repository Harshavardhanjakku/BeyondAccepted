# Problem: Subtract the Product and Sum of Digits of an Integer
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy as np
        return np.prod(list(map(int, str(n)))) - sum(list(map(int, str(n))))

