# Problem: Power of Two
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 5

class Solution(object):
    def isPowerOfTwo(self, n):
        if n==0:
            return False
        if n&n-1==0:
            return True 
        else :
            return False
