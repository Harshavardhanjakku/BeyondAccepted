# Problem: Removing Stars From a String
# Difficulty: Medium
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        nl=[]
        for i in range(len(s)):
            if s[i]=='*':
                nl.pop() 
            else:
                nl.append(s[i])
        return ''.join(nl) 

