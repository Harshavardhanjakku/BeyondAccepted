# Problem: N-th Tribonacci Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 4

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t0=0
        t1=1
        t2=1
        s=0
        if n==0:
            return t0
        elif n==1:
            return t1
        elif n==2:
            return t2
        else:
            for i in range(3,n+1):
                s=t0+t1+t2
                t0=t1
                t1=t2
                t2=s
            return s
        
        
        
