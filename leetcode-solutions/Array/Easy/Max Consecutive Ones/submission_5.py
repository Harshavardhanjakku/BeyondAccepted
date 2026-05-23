# Problem: Max Consecutive Ones
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==0:
                l=r+1
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi

