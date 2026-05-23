# Problem: Single Number II
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        n = len(nums)
        i = 0
        while i < n - 2:
            if nums[i] == nums[i+1] == nums[i+2]:
                i += 3
            else:
                return nums[i]
        return nums[-1] 

