# Minimum Size Subarray Sum
# Difficulty: Medium
# Language: python3

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

