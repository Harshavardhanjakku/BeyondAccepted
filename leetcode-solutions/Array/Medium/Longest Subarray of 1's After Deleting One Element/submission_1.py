# Problem: Longest Subarray of 1's After Deleting One Element
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        zc=0
        l=0
        maxlen=0
        for r in range(n):
            if nums[r]==0:
                zc+=1
            if zc>1:
                if nums[l]==0:
                    zc-=1
                l=l+1
            if zc<=1:     
                maxlen=max(maxlen,r-l+1)
        return maxlen-1
        


