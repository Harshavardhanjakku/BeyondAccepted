# Problem: Perfect Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return False
        count=0
        for i in range(1,int(num**0.5)+1):
            if num%i==0 :
                count+=i+num//i
        if count==2*num:
            return True
        else:
            return False
