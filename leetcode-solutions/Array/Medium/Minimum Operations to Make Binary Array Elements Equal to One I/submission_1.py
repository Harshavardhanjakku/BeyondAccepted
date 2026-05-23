# Problem: Minimum Operations to Make Binary Array Elements Equal to One I
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        count = 0

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                count += 1

        return -1 if nums[-1] == 0 or nums[-2] == 0 else count

