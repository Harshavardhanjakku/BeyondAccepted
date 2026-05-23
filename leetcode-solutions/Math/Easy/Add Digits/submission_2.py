# Problem: Add Digits
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(len(str(num))>0):
            if len(str(num))==1:
                return num
            else:
                s=0
                while(num>0):
                    s+=num%10
                    num//=10
                num=s
