# Length of Last Word
# Difficulty: Easy
# Language: python

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis=s.split()
        return len(lis[-1])
        
