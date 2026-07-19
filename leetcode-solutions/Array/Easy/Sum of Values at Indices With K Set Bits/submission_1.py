# Problem: Sum of Values at Indices With K Set Bits
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = 0
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(n):
            dp[i] = dp[i >> 1] + (i & 1)
            if dp[i] == k:
                sums += nums[i]

        return sums
                
