# Problem: Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low <high :
            mid = low + (high - low)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]
