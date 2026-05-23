# Problem: Find the Integer Added to Array I
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s=0
        c=0
        for i,j in zip(nums1,nums2):
            s+=(j-i)
            c+=1
        return s/c
        
