# Problem: N-Repeated Element in Size 2N Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 6

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        li=len(nums)-1
        lmid=li//2
        if nums[lmid]==nums[lmid-1]:
            return nums[lmid]
        else:
            return nums[lmid+1]
        
