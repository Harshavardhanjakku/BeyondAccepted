# Number of Steps to Reduce a Number to Zero
# Difficulty: Easy
# Language: python

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        c=0
        while(num!=0):
            if num%2==1:
                num-=1
            else:
                num//=2
            c=c+1
        return c
