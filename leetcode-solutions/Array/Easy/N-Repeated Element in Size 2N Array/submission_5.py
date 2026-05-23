# Problem: N-Repeated Element in Size 2N Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        li=len(nums)-1
        return nums[li//2] if nums[li//2]==nums[li//2-1] else nums[li//2+1]
        
