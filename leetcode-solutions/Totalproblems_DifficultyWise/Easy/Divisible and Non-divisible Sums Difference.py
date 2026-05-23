# Divisible and Non-divisible Sums Difference
# Difficulty: Easy
# Language: python

class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        return sum([x for x in range(1,n+1) if x%m!=0])-sum([x for x in range(1,n+1) if x%m==0])
        
