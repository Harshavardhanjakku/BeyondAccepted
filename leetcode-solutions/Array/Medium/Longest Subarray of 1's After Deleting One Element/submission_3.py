# Problem: Longest Subarray of 1's After Deleting One Element
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        zc=0
        l=0
        k=1
        maxlen=0
        for r in range(n):
            if nums[r]==0:
                zc+=1
            if zc>k:
                if nums[l]==0:
                    zc-=1
                l=l+1
            if zc<=k:     
                maxlen=max(maxlen,r-l)
        return maxlen
        


