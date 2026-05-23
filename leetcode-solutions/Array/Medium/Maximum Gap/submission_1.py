# Problem: Maximum Gap
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<2:
            return 0
        nums.sort()
        maxi=float('-inf')
        for ind in range(n-1):
            maxi=max(maxi,nums[ind+1]-nums[ind])
        return maxi

