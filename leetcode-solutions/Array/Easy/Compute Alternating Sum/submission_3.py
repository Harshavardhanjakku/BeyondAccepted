# Problem: Compute Alternating Sum
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=0
        flag=True
        for i in nums :
            if flag:
                tot+=i
            else:
                tot-=i
            flag=not flag
        return tot

