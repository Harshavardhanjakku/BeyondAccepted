# Problem: Compute Alternating Sum
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def alternatingSum(self, nums):
        tot = 0
        for i in range(len(nums)):
            if i % 2 :
                tot -= nums[i]
            else:
                tot += nums[i]
        return tot
