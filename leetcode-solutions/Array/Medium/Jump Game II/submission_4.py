# Problem: Jump Game II
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 4

class Solution:
    def jump(self, nums: List[int]) -> int:
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
