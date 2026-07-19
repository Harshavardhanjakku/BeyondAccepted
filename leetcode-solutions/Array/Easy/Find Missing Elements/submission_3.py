# Problem: Find Missing Elements
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n=len(nums)
        start=nums[0]
        end=nums[-1]
        res=[]
        for num in range(1,n):
            l=nums[num-1]
            r=nums[num]
            res.extend([x for x in range(l+1,r)])
        return res
