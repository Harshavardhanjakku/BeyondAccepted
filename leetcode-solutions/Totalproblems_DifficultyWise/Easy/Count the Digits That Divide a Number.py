# Count the Digits That Divide a Number
# Difficulty: Easy
# Language: python

class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        c=0
        l=list(map(int,str(num)))
        for i in l:
            if num%i==0:
                c+=1
        return c




























