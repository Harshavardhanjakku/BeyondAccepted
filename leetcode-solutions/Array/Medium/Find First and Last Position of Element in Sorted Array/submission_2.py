# Problem: Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarysearch(nums,target):
            low=0
            high=len(nums)-1
            while low <= high :
                mid=(low)+(high-low)//2
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                return -1
        def firstbinarysearch(nums,target):
            low=0
            high=len(nums)-1
            res=-1
            while low <= high :
                mid=(low)+(high-low)//2
                if nums[mid]==target:
                    res=mid
                    high=mid-1
                elif target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                return res
        def lastbinarysearch(nums,target):
            low=0
            high=len(nums)-1
            res=-1
            while low <= high :
                mid=(low)+(high-low)//2
                if nums[mid]==target:
                    res=mid
                    low=mid+1
                elif target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                return res
        if binarysearch(nums,target)==-1:
            return [-1,-1]
        else:
            return [firstbinarysearch(nums,target),lastbinarysearch(nums,target)]


