# Problem: Find Minimum in Rotated Sorted Array II
# Difficulty: Hard
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findMin(self, nums):
        low=0
        high=len(nums)-1
        while low<high:
            mid=low+(high-low)//2
            if nums[mid]>nums[high]:
                low=mid+1
            elif nums[mid]<nums[high]:
                high=mid
            else:
                high-=1
        return nums[low]
