# Minimum Operations to Make Array Sum Divisible by K
# Difficulty: Easy
# Language: python

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(nums)%k
