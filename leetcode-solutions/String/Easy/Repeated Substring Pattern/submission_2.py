# Problem: Repeated Substring Pattern
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        for i in range(1+n//2):
            sub=s[:i]
            if s.replace(sub,"")=="":
                return True
        return False
