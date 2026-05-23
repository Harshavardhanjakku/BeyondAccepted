# Maximum Sum With Exactly K Elements 
# Difficulty: Easy
# Language: python

class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=max(nums)
        s=k*n
        for i in range(k):
            s+=i
        return s
        
