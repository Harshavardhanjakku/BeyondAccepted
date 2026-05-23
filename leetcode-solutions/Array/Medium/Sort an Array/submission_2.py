# Problem: Sort an Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        low=0
        high=len(nums)-1
        def divide(nums,low,high):
            if low>=high:
                return 
            mid=low+(high-low)//2
            divide(nums,low,mid)
            divide(nums,mid+1,high)
            merge(nums,low,mid,high)
        def merge(nums,low,mid,high):
            templen=high-low+1
            temp=[0]*(templen)
            idx=0
            i=low
            j=mid+1
            while i<=mid and j<=high:
                if nums[i]<nums[j]:
                    temp[idx]=nums[i]
                    i+=1
                else:
                    temp[idx]=nums[j]
                    j+=1
                idx+=1
            while i<=mid:
                temp[idx]=nums[i]
                i+=1
                idx+=1
            while j<=high:
                temp[idx]=nums[j]
                j+=1
                idx+=1
            
            for k in range(templen):
                nums[low+k]=temp[k]
        divide(nums,low,high)
        return nums
                
