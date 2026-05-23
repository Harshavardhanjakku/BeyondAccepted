# Problem: The Two Sneaky Numbers of Digitville
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                res.append(nums[i])
                i+=1
        return res
