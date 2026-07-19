# Problem: Maximum Ascending Subarray Sum
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        n = len(nums)
        curr = 0
        for i in range(n - 1):
            curr += nums[i]
            if nums[i] >= nums[i + 1]:
                res = max(res, curr)
                curr = 0
        curr += nums[-1]
        res = max(res, curr)
        return res
