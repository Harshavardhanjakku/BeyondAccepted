# Harshad Number
# Difficulty: Easy
# Language: python

class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        temp=x
        while(x>0):
            s+=x%10
            x//=10
        return s if temp%s==0 else -1

