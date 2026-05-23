# Contains Duplicate
# Difficulty: Easy
# Language: python

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m=len(nums)
        n=len(set(nums))
        return False if m==n else True
        
