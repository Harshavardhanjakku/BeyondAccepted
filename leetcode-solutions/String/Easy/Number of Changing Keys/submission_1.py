# Problem: Number of Changing Keys
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.lower()
        c=0
        n=len(s)
        for i in range(n-1):
            if s[i]!=s[i+1]:
                c+=1
        return c
        
