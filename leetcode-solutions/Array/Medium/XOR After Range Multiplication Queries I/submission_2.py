# Problem: XOR After Range Multiplication Queries I
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD=10**9 + 7
        for query in queries:
            l,r,k,v=query
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k
        xor=0
        for i in nums :
            xor^=i
        return xor
