# Find All Numbers Disappeared in an Array
# Difficulty: Easy
# Language: python

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in nums:
            idx = abs(i) - 1
            nums[idx] = -abs(nums[idx])
        
        return [idx+1 for idx, x in enumerate(nums) if x > 0]

