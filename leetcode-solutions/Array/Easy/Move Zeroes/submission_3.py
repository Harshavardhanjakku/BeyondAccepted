# Problem: Move Zeroes
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        n=len(nums)
        for j in range(n):
            if nums[i]==0:
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
            else:
                i=i+1


        
        
