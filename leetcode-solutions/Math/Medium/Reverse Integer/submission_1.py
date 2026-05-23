# Problem: Reverse Integer
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=1
        if x<0:
            flag=0
            x*=-1
        rev=0
        l=-2147483647
        g=2147483647
        while(x>0):
            r=x%10
            rev=rev*10+r
            x=x//10
        if flag==0:
            rev=rev*-1
        if rev>l and rev<g:
            return rev
        else:
            return 0
        
        
