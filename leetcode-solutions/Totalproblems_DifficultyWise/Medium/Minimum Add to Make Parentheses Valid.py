# Minimum Add to Make Parentheses Valid
# Difficulty: Medium
# Language: python

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        while(s!=""):
            if "()" in s:
                s=s.replace("()","")
            else:
                return len(s)
        return 0
