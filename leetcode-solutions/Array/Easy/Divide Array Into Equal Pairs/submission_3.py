# Problem: Divide Array Into Equal Pairs
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in nums:
            if nums.count(i)%2!=0:
                return False
        return True
