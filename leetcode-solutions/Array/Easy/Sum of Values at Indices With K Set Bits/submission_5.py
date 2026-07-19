# Problem: Sum of Values at Indices With K Set Bits
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tot = 0
        for i in range(len(nums)):
            count = 0
            temp = i
            while temp:
                temp &= (temp - 1)
                count += 1
            if count == k:
                tot += nums[i]
        return tot
