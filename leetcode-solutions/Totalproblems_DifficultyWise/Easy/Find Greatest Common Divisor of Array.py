# Find Greatest Common Divisor of Array
# Difficulty: Easy
# Language: python

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a,b):
            if b%a==0:
                return a
            else:
                return gcd(b%a,a)
        a=min(nums)
        b=max(nums)
        return gcd(a,b)
