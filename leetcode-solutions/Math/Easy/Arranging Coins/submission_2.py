# Problem: Arranging Coins
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        stair=0
        i=1
        while i<=n:
            n-=i
            stair+=1
            i+=1
        return stair
