# Problem: Final Array State After K Multiplication Operations I
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for operation in range(k):
            minvalue=min(nums)
            idx=nums.index(minvalue)
            nums[idx]=minvalue*multiplier
        return nums
