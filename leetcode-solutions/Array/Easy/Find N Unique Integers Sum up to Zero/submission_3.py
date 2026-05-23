# Problem: Find N Unique Integers Sum up to Zero
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        if n%2==1:
            l.append(0)
        for i in range(1,n//2+1):
            l.append(i)
            l.append(-i)
        return l
