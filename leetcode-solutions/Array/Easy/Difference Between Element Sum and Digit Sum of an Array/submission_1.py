# Problem: Difference Between Element Sum and Digit Sum of an Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nw=[sum(list(map(int,str(i)))) for i in nums]
        return abs(sum(nums)-sum(nw))
