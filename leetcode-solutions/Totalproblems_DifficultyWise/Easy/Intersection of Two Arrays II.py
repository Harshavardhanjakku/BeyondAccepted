# Intersection of Two Arrays II
# Difficulty: Easy
# Language: python

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s=set(nums1).intersection(set(nums2))
        nl=[]
        for i in s:
            if i in nums1 and nums2:
                c1=nums1.count(i)
                c2=nums2.count(i)
                nl.extend([i]*c1 if c1<c2 else [i]*c2)
        return nl

