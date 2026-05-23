# Problem: Find Unique Binary String
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findDifferentBinaryString(self, nums):
        dic={}
        length=len(nums[0])
        for x in nums:
            dic[x]=True
        for i in range(0,2**length):
            s=bin(i)[2:].zfill(length)
            if s not in dic:
                return s
