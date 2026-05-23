# Problem: Single Number II
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def singleNumber(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num, count in freq.items():
            if count == 1:
                return num

