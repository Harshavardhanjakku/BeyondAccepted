# Arranging Coins
# Difficulty: Easy
# Language: python

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        res=low
        while low<=high:
            mid=low+(high-low)//2
            if mid*(mid+1)//2<=n:
                res=mid
                low=mid+1
            else:
                high=mid-1
        return res
