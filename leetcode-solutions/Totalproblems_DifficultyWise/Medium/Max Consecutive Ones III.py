# Max Consecutive Ones III
# Difficulty: Medium
# Language: python

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        zc=0
        l=0
        maxlen=0
        for r in range(n):
            if nums[r]==0:
                zc+=1
            if zc>k:
                if nums[l]==0:
                    zc-=1
                l=l+1
            if zc<=k:     
                maxlen=max(maxlen,r-l+1)
        return maxlen
        


