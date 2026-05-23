# Problem: Clumsy Factorial
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=""+str(n)
        k=0
        n-=1
        while n:
            if k==0:
                res+="*"
            elif k==1:
                res+="/"
            elif k==2:
                res+="+"            
            elif k==3:
                res+="-"
            res+=str(n)
            n-=1
            k=(k+1)%4
        print(res)
        return eval(res)
