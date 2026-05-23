# Problem: Maximum Count of Positive Integer and Negative Integer
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        low=0
        high=n-1
        neg=-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]<0:
                neg=mid
                low=mid+1
            else:
                high=mid-1
        nofneg=neg+1
        low=0
        high=n-1
        pos=-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>0:
                pos=mid
                high=mid-1
            else:
                low=mid+1
        nofpos=n-pos if pos != -1 else 0
        return max(nofpos,nofneg)
