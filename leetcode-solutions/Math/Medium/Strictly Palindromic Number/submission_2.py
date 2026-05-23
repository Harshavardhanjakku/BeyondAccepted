# Problem: Strictly Palindromic Number
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=int(bin(n)[2::])
        temp=n
        rev=0
        while n>0:
            rev=rev*10+(n%10)
            n//=10
        return temp==n
        
