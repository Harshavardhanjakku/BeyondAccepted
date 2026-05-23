# Problem: Valid Parentheses
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 10

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while(len(s)>0):
            if '{}' in s:
                s=s.replace('{}','')
            elif '[]' in s:
                s=s.replace('[]','')
            elif '()' in s:
                s=s.replace('()','')
            else:
                return False
        return True
