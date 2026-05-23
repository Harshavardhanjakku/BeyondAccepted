# Problem: Divisible and Non-divisible Sums Difference
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        dn=sum([x for x in range(1,n+1) if x%m==0])
        ndn=sum([x for x in range(1,n+1) if x%m!=0])
        return ndn-dn
        
