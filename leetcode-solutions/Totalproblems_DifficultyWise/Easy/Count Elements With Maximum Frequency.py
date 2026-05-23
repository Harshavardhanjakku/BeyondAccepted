# Count Elements With Maximum Frequency
# Difficulty: Easy
# Language: python

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fl=[nums.count(x) for x in set(nums)]
        no=max(fl)
        return no*fl.count(no)
