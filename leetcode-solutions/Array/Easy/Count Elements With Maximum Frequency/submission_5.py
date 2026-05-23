# Problem: Count Elements With Maximum Frequency
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fl=[nums.count(x) for x in set(nums)]
        no=max(fl)
        return no*fl.count(no)
