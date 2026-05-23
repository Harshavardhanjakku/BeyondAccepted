# Problem: Reverse Degree of a String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 4

class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        tot=0
        for idx in range(len(s)): 
            rev=26-(ord(s[idx])-97)
            tot+=(rev*(idx+1))
        return tot

