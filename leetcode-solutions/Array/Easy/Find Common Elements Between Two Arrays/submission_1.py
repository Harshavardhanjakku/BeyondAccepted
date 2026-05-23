# Problem: Find Common Elements Between Two Arrays
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans1=0
        for i in nums1:
            if i in nums2:
                ans1+=1
        ans2=0
        for i in nums2:
            if i in nums1:
                ans2+=1
        return [ans1,ans2]
        
