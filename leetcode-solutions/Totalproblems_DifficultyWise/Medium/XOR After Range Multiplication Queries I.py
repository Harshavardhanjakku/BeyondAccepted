# XOR After Range Multiplication Queries I
# Difficulty: Medium
# Language: python

class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
        
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor
