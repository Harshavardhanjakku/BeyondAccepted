# Problem: Number of 1 Bits
# Difficulty: Easy
# Topic: Divide and Conquer
# Language: python
# Submission: 3

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        for i in range(32):
            if n&1:
                c+=1
            if n==0:
                break
            n=n>>1
        return c
