# Problem: Search Insert Position
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            for i in range(0,len(nums)):
                if  target<nums[i]:
                    return i
            return len(nums)
        
