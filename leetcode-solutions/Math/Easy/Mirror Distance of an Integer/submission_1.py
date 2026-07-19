# Problem: Mirror Distance of an Integer
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp=n
        rev=0
        while temp>0:
            rev=rev*10+(temp%10)
            temp//=10
        return abs(n-rev)
