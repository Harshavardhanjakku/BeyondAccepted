# Problem: Integer Replacement
# Difficulty: Medium
# Topic: Dynamic Programming
# Language: python
# Submission: 2

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def myfun(n,count):
            if n==1:
                return count
            if n%2==0:
                return myfun(n//2,count+1)
            else:
                return min(myfun(n+1,count+1),myfun(n-1,count+1))
        return myfun(n,0)
        
