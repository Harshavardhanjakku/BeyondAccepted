# Problem: Kth Largest Element in an Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums) 
        return nums[-k]
