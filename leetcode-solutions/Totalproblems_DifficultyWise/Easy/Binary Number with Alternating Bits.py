# Binary Number with Alternating Bits
# Difficulty: Easy
# Language: python

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag=n&1
        while n:
            if flag!=n&1:
                return False
            flag=1-flag
            n=n>>1
        return True
