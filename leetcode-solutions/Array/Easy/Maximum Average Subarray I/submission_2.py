# Problem: Maximum Average Subarray I
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        maxi=tot=sum(nums[:k])
        for i in range(1,n-k+1):
            tot-=nums[i-1]
            tot+=nums[i+k-1]
            maxi=max(maxi,tot)
        return maxi/float(k)
        
