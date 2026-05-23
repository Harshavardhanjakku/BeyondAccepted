# Problem: Minimum Average of Smallest and Largest Elements
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        n=len(nums)
        a=max(nums)
        for i in range(n//2):
            t=sum([nums[i],nums[n-i-1]])/2.0
            if t<a:
                a=t
        return a
        
