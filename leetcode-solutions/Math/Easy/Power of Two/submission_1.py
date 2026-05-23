# Problem: Power of Two
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0
