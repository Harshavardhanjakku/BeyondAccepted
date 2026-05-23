# Problem: Remove Trailing Zeros From a String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        return str(int(num[::-1]))[::-1]
