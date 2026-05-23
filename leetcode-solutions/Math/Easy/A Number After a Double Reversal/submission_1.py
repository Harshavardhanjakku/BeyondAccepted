# Problem: A Number After a Double Reversal
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num>=-9 and num<=9:
            return True
        else:
            return True if num%10!=0 else False
        
