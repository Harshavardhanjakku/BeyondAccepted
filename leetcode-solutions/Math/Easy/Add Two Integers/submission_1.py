# Problem: Add Two Integers
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        return (num1^num2)+2*(num1&num2)
