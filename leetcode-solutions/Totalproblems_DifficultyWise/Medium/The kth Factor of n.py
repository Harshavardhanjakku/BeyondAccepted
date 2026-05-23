# The kth Factor of n
# Difficulty: Medium
# Language: python

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        fl=[]
        for i in range(1,n//2+1):
            if n%i==0:
                fl.append(i)
        fl.append(n)
        if len(fl)<k:
            return -1
        else:
            return fl[k-1]

