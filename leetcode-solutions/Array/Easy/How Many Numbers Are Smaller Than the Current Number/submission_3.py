# Problem: How Many Numbers Are Smaller Than the Current Number
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cl=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if i!=j and nums[j]<nums[i]:
                    c+=1
            cl.append(c)
        return cl
                    
