# Problem: Kids With the Greatest Number of Candies
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        largest=max(candies)
        return [x+extraCandies>=largest for x in candies]
