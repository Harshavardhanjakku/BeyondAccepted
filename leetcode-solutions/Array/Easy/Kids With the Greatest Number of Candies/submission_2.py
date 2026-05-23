# Problem: Kids With the Greatest Number of Candies
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        return [x+extraCandies>=max(candies) for x in candies]
