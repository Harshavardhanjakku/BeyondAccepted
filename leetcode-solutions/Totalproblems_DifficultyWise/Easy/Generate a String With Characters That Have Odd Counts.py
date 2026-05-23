# Generate a String With Characters That Have Odd Counts
# Difficulty: Easy
# Language: python

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        return n*"a" if n%2 else (n-1)*"a"+"b"
