# Problem: Remove Element
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def removeElement(self, nums, val):
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[j]==val:
                j-=1
            elif nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
            else:
                i+=1
        return j+1
