# Problem: Integer Replacement
# Difficulty: Medium
# Topic: Dynamic Programming
# Language: python
# Submission: 1

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        def myfun(n):
            if n==1:
                return 0
            if n in memo:
                return memo[n]
            if n%2==0:
                memo[n]=1+myfun(n//2) 
            else:
                memo[n]=1+min(myfun(n+1 ),myfun(n-1 ))
            return memo[n]
        return myfun(n)
        
