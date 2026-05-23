# Problem: Majority Element
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def majorityElement(self, nums):
        nums=sorted(nums)
        return(nums[len(nums)//2])
        
