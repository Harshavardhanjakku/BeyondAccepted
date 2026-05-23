# Count Number of Pairs With Absolute Difference K
# Difficulty: Easy
# Language: python

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if abs(nums[i]-nums[j])==k:
                    c+=1
        return c
