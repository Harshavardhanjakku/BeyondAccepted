# Problem: Sum of Two Integers
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a < 0 or b<0 :
            return a+b
        result=0
        exponent=0
        ans=0
        carry=0
        while a>0 or b>0 :
            abit=a&1
            bbit=b&1
            total=abit+bbit+carry
            if total==3:
                ans=1
                carry=1
            elif total==2:
                ans=0
                carry=1
            else:
                carry=0
                ans=total
            result+=(1<<exponent)*ans
            exponent+=1
            a=a>>1
            b=b>>1
        if carry:
            result+=1<<exponent
        return result
