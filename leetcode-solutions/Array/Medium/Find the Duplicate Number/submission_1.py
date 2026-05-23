# Problem: Find the Duplicate Number
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=True
            else:
                return i
                 

