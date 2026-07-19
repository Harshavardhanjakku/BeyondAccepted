# Problem: Single Number III
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in nums :
            freq[i]=freq.get(i,0)+1
        res=[]
        for i in freq:
            if freq[i]==1:
                res.append(i)
        return res
