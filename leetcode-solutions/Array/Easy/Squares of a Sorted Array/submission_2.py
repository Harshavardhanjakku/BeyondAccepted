# Problem: Squares of a Sorted Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        i,j,ind=0,n-1,n-1
        res=[0]*n
        while i<=j:
            if nums[j]*nums[j]>nums[i]*nums[i]:
                res[ind]=nums[j]*nums[j]
                j-=1
            else :
                res[ind]=nums[i]*nums[i]
                i+=1
            ind-=1
        return res
