# Problem: Generate a String With Characters That Have Odd Counts
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        return n*"a" if n%2 else (n-1)*"a"+"b"
