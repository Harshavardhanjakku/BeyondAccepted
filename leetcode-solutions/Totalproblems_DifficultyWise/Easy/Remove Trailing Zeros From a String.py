# Remove Trailing Zeros From a String
# Difficulty: Easy
# Language: python

class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        return str(int(num[::-1]))[::-1]
