# Problem: Maximum Subarray
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        curr=maxi=nums[0]
        for i in range(1,n):
            curr=max(nums[i],curr+nums[i])
            maxi=max(curr,maxi)
        return maxi
