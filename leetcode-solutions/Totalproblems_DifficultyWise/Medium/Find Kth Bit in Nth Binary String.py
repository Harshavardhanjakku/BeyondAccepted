# Find Kth Bit in Nth Binary String
# Difficulty: Medium
# Language: python

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def func(n):
            if n==1:
                return "0"
            else:
                t=func(n-1)
                inv=t.replace("1","c")
                inv=inv.replace("0","1")
                inv=inv.replace("c","0")
                return t+"1"+inv[::-1]
        word=func(n)
        return word[k-1]
