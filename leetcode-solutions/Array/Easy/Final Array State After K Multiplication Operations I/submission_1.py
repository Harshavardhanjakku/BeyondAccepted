# Problem: Final Array State After K Multiplication Operations I
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            x=nums.index(min(nums))
            nums[x]*=multiplier
        return nums
