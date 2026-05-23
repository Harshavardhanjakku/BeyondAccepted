# Problem: Number of 1 Bits
# Difficulty: Easy
# Topic: Divide and Conquer
# Language: python
# Submission: 2

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        while n>0:
            if n&1:
                c+=1
            n=n>>1
        return c
