# Problem: Happy Number
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 3

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(True):
            s=0
            while(n>0):
                s+=(n%10)**2
                n//=10
            n=s
            if len(str(n))==1:
                break
        if n==1 or n==7:
            return True
        else:
            return False
        
