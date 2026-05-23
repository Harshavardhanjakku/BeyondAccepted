# Problem: Find All Numbers Disappeared in an Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        for i in nums :
            dic[i]=True
        n=len(nums)
        return [num for num in range(1,n+1) if num not in dic ]
