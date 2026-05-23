# Problem: Base 7
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        flag=False
        s=""
        if num<0 :
            flag=True
            num*=-1 
        while num>0 :
            rem=num%7
            num=num//7
            s+=str(rem)
        return "-"+s[::-1] if flag else s[::-1] 
