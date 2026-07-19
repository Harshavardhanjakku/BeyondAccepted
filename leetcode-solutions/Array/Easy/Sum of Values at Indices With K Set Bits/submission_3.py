# Problem: Sum of Values at Indices With K Set Bits
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        tot = 0
        for i in range(n):
            if dp[i] == k:
                tot += nums[i]
        return tot
