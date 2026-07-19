# Problem: Sum of Values at Indices With K Set Bits
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        dp=[-1]*(n+1)
        def setBits(n):
            if n==0:
                return 0
            elif dp[n]!=-1:
                return dp[n]
            dp[n]=setBits(n//2)+(n%2)
            return dp[n] 
        tot=0
        for i in range(n):
            if setBits(i)==k:
                tot+= nums[i]
        return tot
