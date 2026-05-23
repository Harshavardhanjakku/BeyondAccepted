# Problem: Alternating Digit Sum
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sign=-1 if len(str(n))%2==0 else 1
        res=0
        while(n>0):
            res+=(n%10)*sign
            sign*=-1
            n//=10
        return res

            

        
