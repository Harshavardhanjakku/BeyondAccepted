# Problem: Longest Continuous Increasing Subsequence
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n<2: return n
        maxi = 0
        for i in range(n - 1):
            length = 1
            for j in range(i, n - 1):
                if nums[j]< nums[j + 1]:
                    length += 1
                else:
                    break
            maxi = max(maxi, length)
        return maxi
