# Problem: N-Repeated Element in Size 2N Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        for i in nums:
            if i in s :
                return i 
            else:
                s.add(i)
