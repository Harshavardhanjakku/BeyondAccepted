# Problem: Max Consecutive Ones
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=0
        count=0
        for i in nums :
            if i==0:
                count=0
            elif i==1:
                count+=1
            maxi=max(maxi,count)
        return maxi
