# Problem: Sum of All Subset XOR Totals
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=0
        n=len(nums)
        res=[]
        for i in range(1<<n):
            temp=0
            for j in range(n):
                if (i>>j)&1==1:
                    temp^=nums[j]
            if temp:
                tot+=temp
        return tot
