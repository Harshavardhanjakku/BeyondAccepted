# Problem: Merge Sorted Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res=[0]*(m+n)
        i,j=0,0
        idx=0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                res[idx]=nums1[i]
                i+=1
            else:
                res[idx]=nums2[j]
                j+=1
            idx+=1
        while i<m:
            res[idx]=nums1[i]
            i+=1
            idx+=1
        while j<n:
            res[idx]=nums2[j]
            j+=1
            idx+=1
        nums1[:]=res
