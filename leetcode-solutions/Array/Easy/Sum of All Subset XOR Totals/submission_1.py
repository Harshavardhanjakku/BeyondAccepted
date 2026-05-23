# Problem: Sum of All Subset XOR Totals
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=0
        n=len(nums)
        for x in nums :
            tot|=x
        return tot * (1<<(n-1))
