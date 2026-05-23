# Problem: Determine if String Halves Are Alike
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        n=len(s)//2
        ac=0
        bc=0
        v="aeiou"
        for i in range(0,n):
            if s[i] in v:
                ac+=1
            if s[n+i] in v:
                bc+=1
        if ac==bc:
            return True
        else:
            return False


        
