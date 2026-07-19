# Problem: Concatenate Non-Zero Digits and Multiply by Sum I
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n :
            return 0
        s=str(n)
        s=s.replace("0","")
        tot=0
        for i in s:
            tot+=int(i)
        return int(s)*tot
