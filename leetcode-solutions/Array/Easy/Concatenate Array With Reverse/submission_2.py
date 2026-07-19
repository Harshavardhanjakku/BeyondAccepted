# Problem: Concatenate Array With Reverse
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums[::-1])
        return nums
