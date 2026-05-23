# How Many Numbers Are Smaller Than the Current Number
# Difficulty: Easy
# Language: python

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortednums=sorted(nums)
        idx=0
        dic={}
        for i in sortednums:
            if i not in dic :
                dic[i]=idx
            idx+=1
        return [dic[i] for i in nums ]

