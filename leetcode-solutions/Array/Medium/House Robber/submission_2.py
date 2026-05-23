# Problem: House Robber
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1] * n    
        def find(n):
            if n < 0:
                return 0
            elif n == 0:
                return nums[0]
            elif dp[n] != -1:   
                return dp[n]
            dp[n] = max(find(n-1), nums[n] + find(n-2))
            return dp[n]
        
        return find(n-1)
