# Problem: Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if self.binarysearch(nums,target)==-1:
            return [-1,-1]
        else:
            l=self.firstoccur(nums,target)
            h=self.lastoccur(nums,target)
            return [l,h]
            
    def binarysearch(self,nums,target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                high=mid-1
            else :
                low=mid+1 
        else:
            return -1    

    def lastoccur(self,l,ele):
        low = 0
        high = len(l) - 1
        result = -1
        while low <= high:
            mid = low + (high - low) // 2
            if l[mid] == ele:
                result = mid       
                low = mid + 1      
            elif l[mid] < ele:
                low = mid + 1
            else:
                high = mid - 1
        return result
    def firstoccur(self,l,ele):
        low = 0
        high = len(l) - 1
        result = -1
        while low <= high:
            mid = low + (high - low) // 2
            if l[mid] == ele:
                result = mid       
                high = mid - 1      
            elif l[mid] < ele:
                low = mid + 1
            else:
                high = mid - 1
        return result
