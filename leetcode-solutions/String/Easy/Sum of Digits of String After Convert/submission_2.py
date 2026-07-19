# Problem: Sum of Digits of String After Convert
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def getLucky(self,s,k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res=0

        for i in s:
            r=ord(i)-96
            if r<10:
                res=res*10+r
            else:
                res=res*100+r

        count=0

        while count<k:
            tot=0
            temp=res
            while temp>0:
                tot+=temp%10
                temp//=10
            res=tot
            count+=1

        return res
