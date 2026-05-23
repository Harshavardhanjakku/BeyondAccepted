# Problem: Jump Game II
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def jump(self, nums: List[int]) -> int:
        l=0
        r=0
        jump=0
        n=len(nums)-1
        flag=False
        while r<n:
            m=0
            for i in range(l,r+1):
                if nums[i]+i>m:
                    m=nums[i]+i
                if m>=n:
                    flag=True
                    break

            l=r+1
            r=m
            jump=jump+1
            if flag:
                break
        return jump
