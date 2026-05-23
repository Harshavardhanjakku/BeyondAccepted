# Problem: Rotate Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def myrev(start,end):
            i=start
            j=end
            while i<j :
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        n=len(nums)
        k=k%n
        if n==1:
            return
        myrev(0,n-1)
        myrev(0,k-1)
        myrev(k,n-1)
        
