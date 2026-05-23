# Problem: Nim Game
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0
