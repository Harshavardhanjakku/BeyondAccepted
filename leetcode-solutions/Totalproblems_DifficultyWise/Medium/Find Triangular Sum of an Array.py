# Find Triangular Sum of an Array
# Difficulty: Medium
# Language: python

class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for length in range(n,1,-1):
            for i in range(length-1):
                nums[i]=(nums[i]+nums[i+1])%10
        return nums[0]
