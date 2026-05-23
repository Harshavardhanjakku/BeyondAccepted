# Median of Two Sorted Arrays
# Difficulty: Hard
# Language: python

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        totlen=m+n
        res=[]
        i=j=0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        if i<m :
            res.extend(nums1[i:])
        if j<n:
            res.extend(nums2[j:])
        avg=res[totlen//2] if totlen%2 else (res[totlen//2]+res[totlen//2-1])/2.0
        return avg
