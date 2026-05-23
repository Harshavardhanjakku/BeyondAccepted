# Separate the Digits in an Array
# Difficulty: Easy
# Language: python

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums:
            temp=[]
            while i>0:
                temp.append(i%10)
                i//=10
            res.extend(temp[::-1])
        return res
