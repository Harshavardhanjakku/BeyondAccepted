# Problem: Check Good Integer
# Difficulty: Easy
# Topic: Other
# Language: python
# Submission: 1

class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        squareSum=0
        digitSum=0
        while n > 0: 
            r=n%10
            squareSum+=r*r
            digitSum+=r
            n//=10
        return squareSum-digitSum>=50
