# Problem: Minimum Operations to Make the Array Increasing
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        else:
            s=0
            n=len(nums)
            nl=[nums[0]]
            for i in range(1,n):
                if nums[i]<=nums[i-1]:
                    s+=nums[i-1]-nums[i]+1
                    nums[i]=nums[i-1]+1
            return s


