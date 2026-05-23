# Sum of Squares of Special Elements 
# Difficulty: Easy
# Language: python

class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=0
        for i in range(n):
            if n%(i+1)==0:
                s+=nums[i]**2
        return s
