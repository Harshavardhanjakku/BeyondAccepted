# Problem: Count Integers With Even Digit Sum
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        for i in range(1,num+1):
            s=0
            temp=i
            while(temp>0):
                s+=temp%10
                temp//=10
            if s%2==0:
                count+=1
        return count
