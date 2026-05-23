# Problem: Difference Between Element Sum and Digit Sum of an Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nw=[]
        for i in nums:
            nw.append(sum(list(map(int,str(i)))))
        return abs(sum(nums)-sum(nw))
