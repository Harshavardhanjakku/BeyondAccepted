# Problem: Product of Array Except Self
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        pro=1
        zflag=False
        lp=[0]*n
        rp=[0]*n
        rpro=1
        for i in range(n):
            ind=-(i+1)
            rpro*=nums[ind]
            if nums[i]==0:
                zflag=True
            pro*=nums[i]
            lp[i]=pro
            rp[ind]=rpro
        if not zflag:
            return [pro//x for x in nums]
        else:
            res=[0]*n
            res[0]=rp[1]
            res[-1]=lp[-2]
            for i in range(1,n-1):
                res[i]=rp[i+1]*lp[i-1]
            return res


