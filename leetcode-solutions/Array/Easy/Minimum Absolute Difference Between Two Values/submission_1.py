# Problem: Minimum Absolute Difference Between Two Values
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        res=101
        flag=False
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==3:
                    flag=True
                    res=min(res,j-i)
        return res if flag else -1
