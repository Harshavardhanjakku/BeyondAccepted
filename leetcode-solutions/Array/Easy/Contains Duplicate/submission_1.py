# Problem: Contains Duplicate
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m=len(nums)
        n=len(set(nums))
        return False if m==n else True
        
