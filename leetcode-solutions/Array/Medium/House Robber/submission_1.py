# Problem: House Robber
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def rob(self, nums):
        a, b = 0, 0
        for i in range(len(nums)):
            temp = a
            a = max(a, b + nums[i]) 
            b = temp
        return a
