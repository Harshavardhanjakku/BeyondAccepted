# Problem: The kth Factor of n
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def checkprime(n):
            count=0
            for i in range(1,n//2+1):
                if n%i==0:
                    count+=1
                if count>2:
                    break
            if count==1:
                return True
            else:
                return False
        def checkfactor(n):
            count=0
            for i in range(1,n//2+1):
                if n%i==0:
                    count+=1
                if count==k:
                    return i
            return n if k==count+1 else -1
        if k==1:
            return 1
        elif k==2:
            if checkprime(n):
                return n
            else:
                res=checkfactor(n)
                return res
        else:
            res=checkfactor(n)
            return res
