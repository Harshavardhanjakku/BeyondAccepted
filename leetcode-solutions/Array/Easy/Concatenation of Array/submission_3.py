# Problem: Concatenation of Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums)
        return nums
