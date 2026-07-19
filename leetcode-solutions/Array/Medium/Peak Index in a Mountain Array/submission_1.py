# Problem: Peak Index in a Mountain Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low = 0
        high = len(arr)-1
        while low <= high :
            mid = low +(high - low )//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid 
            elif arr[mid]>arr[mid+1]:
                high=mid-1
            elif arr[mid+1]>arr[mid]:
                low=mid+1
         
