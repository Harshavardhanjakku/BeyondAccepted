# Problem: Single Number
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        else:
            mySet=set(nums)
            for i in mySet:
                if nums.count(i)==1:
                    return i
