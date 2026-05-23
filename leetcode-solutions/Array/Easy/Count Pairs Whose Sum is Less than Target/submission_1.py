# Problem: Count Pairs Whose Sum is Less than Target
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    c+=1
        return c
