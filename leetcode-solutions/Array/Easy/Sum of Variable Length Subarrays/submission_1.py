# Problem: Sum of Variable Length Subarrays
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=0
        n=len(nums)
        for i in range(n):
            for idx in range(max(0, i - nums[i]),i+1):
                tot+=nums[idx]
        return tot
