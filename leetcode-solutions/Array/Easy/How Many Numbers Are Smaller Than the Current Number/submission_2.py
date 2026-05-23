# Problem: How Many Numbers Are Smaller Than the Current Number
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(nums)
        for i in range(n):
            count=0
            for j in range(n):
                if nums[i]>nums[j]:
                    count+=1
            res.append(count)
        return res
