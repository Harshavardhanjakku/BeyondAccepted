# Divide Array Into Equal Pairs
# Difficulty: Easy
# Language: python

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=set(nums)
        for i in s:
            if nums.count(i)%2!=0:
                return False
        return True
