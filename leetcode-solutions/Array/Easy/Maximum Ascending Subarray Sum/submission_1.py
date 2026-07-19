# Problem: Maximum Ascending Subarray Sum
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def maxAscendingSum(self, nums):
        res = float('-inf')
        curr = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                res = max(res, curr)
                curr = nums[i]

        res = max(res, curr)
        return res
