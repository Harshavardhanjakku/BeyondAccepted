# Count Odd Numbers in an Interval Range
# Difficulty: Easy
# Language: python

class Solution(object):
    def countOdds(self, low, high):
        return (high + 1)//2 - low//2
