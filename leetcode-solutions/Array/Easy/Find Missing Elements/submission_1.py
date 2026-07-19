# Problem: Find Missing Elements
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findMissingElements(self, nums):
        s = set(nums)
        return [i for i in range(min(nums), max(nums) + 1) if i not in s]
