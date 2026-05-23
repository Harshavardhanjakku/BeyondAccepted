# Problem: Power of Two
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 4

class Solution(object):
    def isPowerOfTwo(self, n):
        if n&n-1 or n==0:
            return False 
        return True
