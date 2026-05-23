# Problem: Sort an Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mergesort(nums,0,len(nums)-1)
        return nums
    def mergesort(self,nums,low,high):
        if low<high:
            mid=low+(high-low)//2
            self.mergesort(nums,low,mid)
            self.mergesort(nums,mid+1,high)
            self.merge(nums,low,mid,high)
    def merge(self,arr,low,mid,high):
        final=[]
        i=0
        j=0
        a=arr[low:mid+1]
        b=arr[mid+1:high+1]
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                final.append(a[i])
                i+=1
            else:
                final.append(b[j])
                j+=1
        final.extend(a[i:])
        final.extend(b[j:])
        arr[low:high+1] = final

