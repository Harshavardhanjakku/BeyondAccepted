# Problem: Count Odd Numbers in an Interval Range
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def countOdds(self, low, high):
        return (high + 1)//2 - low//2
