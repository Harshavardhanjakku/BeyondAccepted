# Single Number II
# Difficulty: Medium
# Language: python

class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        n = len(nums)
        i = 1
        while i < n :
            if nums[i]== nums[i-1]:
                i += 3
            else:
                return nums[i-1]
        return nums[-1] 

