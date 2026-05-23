# Problem: Reverse Words in a String
# Difficulty: Medium
# Topic: Two Pointers
# Language: python
# Submission: 2

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split()
        return " ".join(l[::-1])
        
