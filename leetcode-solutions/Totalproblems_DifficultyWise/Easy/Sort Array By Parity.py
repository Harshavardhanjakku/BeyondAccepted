# Sort Array By Parity
# Difficulty: Easy
# Language: python

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evenl=[x for x in nums if x%2==0]
        evenl.extend([x for x in nums if x%2==1 ])
        return evenl
