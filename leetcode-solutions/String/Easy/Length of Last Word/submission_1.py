# Problem: Length of Last Word
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis=s.split()
        return len(lis[-1])
        
