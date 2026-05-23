# Problem: Intersection of Two Arrays
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1).intersection(set(nums2))
