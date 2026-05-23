# Problem: Find Minimum in Rotated Sorted Array II
# Difficulty: Hard
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        for i in nums:
            res=min(res,i)
        return res
