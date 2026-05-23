# Problem: Arranging Coins
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        stair=1
        i=1
        while i<=n:
            n-=i
            stair+=1
            i+=1
        return stair-1
