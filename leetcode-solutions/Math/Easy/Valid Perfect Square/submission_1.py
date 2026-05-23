# Problem: Valid Perfect Square
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return True if (num**0.5)%1==0 else False
        
