# Problem: A Number After a Double Reversal
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 4

class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        frev=int(str(num)[::-1])
        srev=int(str(frev)[::-1])
        return True if srev==num else False
        
