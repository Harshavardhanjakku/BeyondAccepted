# Problem: Separate the Digits in an Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums:
            nl=list(map(int,str(i)))
            for no in nl:
                l.append(no)
        return l
