# Problem: Limit Occurrences in Sorted Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def limitOccurrences(self, nums, k):
        res = []
        curr = nums[0]
        count = 0
        for num in nums:
            if num == curr:
                count += 1
            else:
                curr = num
                count = 1
            if count <= k:
                res.append(num)
        return res
