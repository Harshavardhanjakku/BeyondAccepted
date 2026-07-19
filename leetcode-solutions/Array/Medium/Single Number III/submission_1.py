# Problem: Single Number III
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor ^= n 
        diff = xor & -xor
        a = 0
        b = 0
        for n in nums:
            if n & diff:
                a ^= n
            else:
                b ^= n
        return [a, b]
