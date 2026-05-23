# Neither Minimum nor Maximum
# Difficulty: Easy
# Language: python

class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return -1
        else:
            m=max(nums)
            l=min(nums)
            nums.remove(m)
            nums.remove(l)
            return nums[0]
