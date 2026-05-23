# Summary Ranges
# Difficulty: Easy
# Language: python

class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        a=nums[0]
        b=nums[0]
        n=len(nums)
        res=[]
        for i in range(n-1):
            if nums[i]+1==nums[i+1]:
                b=nums[i+1]
            else:
                if a!=b:
                    s=str(a)+"->"+str(b)
                    res.append(s)
                else:
                    res.append(str(a))
                a=nums[i+1]
                b=nums[i+1]
        if a!=b:
            res.append(str(a)+"->"+str(b))
        else:
            res.append(str(a))
            
        return res
