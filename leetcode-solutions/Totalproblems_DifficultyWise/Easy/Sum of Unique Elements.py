# Sum of Unique Elements
# Difficulty: Easy
# Language: python

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for i in set(nums):
            if nums.count(i)==1:
                s+=i
        return s
        
