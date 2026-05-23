# Problem: Find the Key of the Numbers
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        n1=str(num1)
        n2=str(num2)
        n3=str(num3)
        l=len(n1)
        n1="0"*(4-l) + n1
        m=len(n2)
        n2="0"*(4-m) + n2
        n=len(n3)
        n3="0"*(4-n) + n3
        res="" 
        print(n1,n2,n3)
        for i in range(4):
            mini=min(n1[i],n2[i],n3[i])
            res+=mini
        return int(res)
