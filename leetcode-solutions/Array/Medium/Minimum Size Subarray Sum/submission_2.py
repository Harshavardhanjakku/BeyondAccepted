# Problem: Minimum Size Subarray Sum
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def minSubArrayLen(self,target:int,nums:List[int])->int:
        n=len(nums)
        if sum(nums)<target:
            return 0
        res=n
        i=0
        j=0
        tot=0
        while j<n:
            tot+=nums[j]
            while tot>=target:
                res=min(res,j-i+1)
                tot-=nums[i]
                i+=1
            j+=1
        return res
 
