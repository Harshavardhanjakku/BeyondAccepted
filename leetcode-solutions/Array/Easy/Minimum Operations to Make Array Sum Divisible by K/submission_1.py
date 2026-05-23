# Problem: Minimum Operations to Make Array Sum Divisible by K
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(nums)%k
