# Problem: Maximum Product Difference Between Two Pairs
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return ((nums[-1]*nums[-2])-(nums[0]*nums[1]))
