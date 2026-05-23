# Problem: Jump Game II
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        jump=0
        while r<len(nums)-1:
            m=0
            for i in range(l,r+1):
                if nums[i]+i>m:
                    m=nums[i]+i
            l=r+1
            r=m
            jump=jump+1
        return jump
