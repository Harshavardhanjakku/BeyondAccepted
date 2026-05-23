# Find Minimum Operations to Make All Elements Divisible by Three
# Difficulty: Easy
# Language: python

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            if i%3 in [1,2] or i<3:
                c+=1
        return c
