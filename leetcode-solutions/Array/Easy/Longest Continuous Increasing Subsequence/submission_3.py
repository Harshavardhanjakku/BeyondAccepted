# Problem: Longest Continuous Increasing Subsequence
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        return ans

