# Problem: Maximum Count of Positive Integer and Negative Integer
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        pos=0
        neg=0
        for i in nums:
            if i>0:
                pos+=1
            if i<0:
                neg+=1
        return max(pos,neg)
