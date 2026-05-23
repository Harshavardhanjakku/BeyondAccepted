# Problem: Check if Array Is Sorted and Rotated
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n<3 :
            return True
        if nums[0]<nums[-1]:
            count=0
            for i in range(n-1):
                if nums[i]==nums[i+1]:
                    continue
                elif nums[i]>nums[i+1]:
                    return False 
            return True
        else:
            count=0
            for i in range(n-1):
                if nums[i]==nums[i+1]:
                    continue
                elif nums[i]>nums[i+1]:
                    count+=1
            return count<=1



