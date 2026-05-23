# Find All Duplicates in an Array
# Difficulty: Medium
# Language: python

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i]=True
            else:
                dic[i]=False
        return [x for x in dic.keys() if dic[x]==True]
