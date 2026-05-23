# Problem: Add Digits
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 3

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
                num=sum(list(map(int,str(num))))
