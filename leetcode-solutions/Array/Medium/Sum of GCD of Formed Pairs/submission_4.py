# Problem: Sum of GCD of Formed Pairs
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 4

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        import math
        maxi=max(nums)
        n=len(nums)
        prefix=[0]*n
        curr=float('-inf')
        for i in range(n):
            curr=max(curr,nums[i])
            prefix[i]=curr 
        for i in range(n): 
            prefix[i]=math.gcd(prefix[i],nums[i]) 
        prefix.sort()
        left=0
        right=n-1
        tot=0
        print(prefix)
        while left<right: 
            tot+=math.gcd(prefix[left],prefix[right])
            left+=1
            right-=1
        return tot
