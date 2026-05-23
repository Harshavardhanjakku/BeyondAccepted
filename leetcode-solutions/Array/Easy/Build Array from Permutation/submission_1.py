# Problem: Build Array from Permutation
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(len(nums)):
            l.append(nums[nums[i]])
        return l
        
