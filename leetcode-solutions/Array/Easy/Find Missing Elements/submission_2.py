# Problem: Find Missing Elements
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findMissingElements(self, nums):
        s = set(nums)
        res = []
        for i in range(min(nums), max(nums) + 1):
            if i not in s:
                res.append(i)
        return res
