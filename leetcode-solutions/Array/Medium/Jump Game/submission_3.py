# Problem: Jump Game
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
    """
        n=len(nums)
        if n==1:
            return True 
        if nums[0]==0:
            return False
        curr=nums[0]
        for i in range(1,n):
            curr=curr-1
            if i==n-1:
                return True
            if nums[i]>curr:
                curr=nums[i]
            if curr<=0: 
                return False
        return True
