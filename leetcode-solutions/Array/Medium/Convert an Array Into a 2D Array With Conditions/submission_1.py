# Problem: Convert an Array Into a 2D Array With Conditions
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s=set(nums)
        dic={}
        for i in s:
            dic[i]=nums.count(i)
        m=max(dic.values())
        res=[[] for i in range(m)]
        for i in dic:
            ind=0
            for j in range(dic[i]):
                res[ind].append(i)
                ind+=1
        return res
        
