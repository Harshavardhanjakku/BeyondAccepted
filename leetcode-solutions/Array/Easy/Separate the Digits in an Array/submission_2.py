# Problem: Separate the Digits in an Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(map(int,"".join(map(str,nums))))
