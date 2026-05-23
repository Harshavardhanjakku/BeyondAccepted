# Maximum Product of Two Elements in an Array
# Difficulty: Easy
# Language: python

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fmax=max(nums)
        findex=nums.index(fmax)
        nums[findex]=min(nums)
        smax=max(nums)
        return (fmax-1)*(smax-1)

