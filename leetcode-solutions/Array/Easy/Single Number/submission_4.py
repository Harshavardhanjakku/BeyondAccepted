# Problem: Single Number
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        else:
            for i in nums:
                if nums.count(i)==1:
                    return i
