# Longest Continuous Increasing Subsequence
# Difficulty: Easy
# Language: python

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        count = 1
        n=len(nums)
        for i in range(n- 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        return ans

