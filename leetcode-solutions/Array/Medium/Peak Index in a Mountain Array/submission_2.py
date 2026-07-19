# Problem: Peak Index in a Mountain Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return arr.index(max(arr))
