# Problem: Max Consecutive Ones
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 6

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l=0
        r=0
        maxi=0
        for i in range(n):
            if nums[i]==0:
                l=r+1
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi

