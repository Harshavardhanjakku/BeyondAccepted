# Problem: Minimum Size Subarray Sum
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def minSubArrayLen(self,target:int,nums:List[int])->int:
        s=0
        left=0
        ans=float('inf')
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                ans=min(ans,i-left+1)
                s-=nums[left]
                left+=1
        return 0 if ans==float('inf') else ans

