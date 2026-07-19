# Problem: Distribute Candies
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def distributeCandies(self, candyType):
        return min(len(set(candyType)), len(candyType) // 2)
