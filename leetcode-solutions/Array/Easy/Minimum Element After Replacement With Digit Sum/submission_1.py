# Problem: Minimum Element After Replacement With Digit Sum
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            temp=nums[i]
            s=0
            while(temp>0):
                s+=temp%10
                temp//=10
            nums[i]=s
        return min(nums)
