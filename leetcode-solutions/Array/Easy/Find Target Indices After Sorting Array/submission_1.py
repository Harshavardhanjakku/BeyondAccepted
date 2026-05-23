# Problem: Find Target Indices After Sorting Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums=sorted(nums)
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        return l
