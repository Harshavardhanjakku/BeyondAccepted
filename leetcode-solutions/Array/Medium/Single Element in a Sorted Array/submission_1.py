# Problem: Single Element in a Sorted Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in nums:
            res^=i
        return res
