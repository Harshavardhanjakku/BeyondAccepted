# Problem: Count Odd Numbers in an Interval Range
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        a=low if low%2 else low+1
        l=high if high%2 else high-1
        return 1+(l-a)//2

