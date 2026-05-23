# Reverse Words in a String
# Difficulty: Medium
# Language: python

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split()
        return " ".join(l[::-1])
        
