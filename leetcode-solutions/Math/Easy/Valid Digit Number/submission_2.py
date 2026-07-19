# Problem: Valid Digit Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        flag=False
        r=0
        while n :
            r=n%10
            if r==x:
                flag=True
            n//=10
        return r!=x and flag
