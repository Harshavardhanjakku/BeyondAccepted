# Problem: Remove Trailing Zeros From a String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        num=int(num[::-1])
        return str(num)[::-1]
