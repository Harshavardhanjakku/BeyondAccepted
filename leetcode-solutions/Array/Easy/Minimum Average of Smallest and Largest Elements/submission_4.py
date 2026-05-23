# Problem: Minimum Average of Smallest and Largest Elements
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        step=0
        avg=[]
        l=len(nums)
        while step<l//2:
            m=min(nums)
            n=max(nums)
            nums.remove(m)
            nums.remove(n)
            avg.append((m+n)/2.0)
            step+=1
        return min(avg)
        
