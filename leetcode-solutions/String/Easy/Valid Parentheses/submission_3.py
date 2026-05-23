# Problem: Valid Parentheses
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 3

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while s!="":
            if "()" in s:
                s=s.replace("()","")
            elif "{}" in s:
                s=s.replace("{}","")
            elif "[]" in s:
                s=s.replace("[]","")
            else :
                return False
        else:
            return True
