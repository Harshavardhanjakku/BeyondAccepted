# Problem: Find the Difference
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution:
    def findTheDifference(self, s, t):
        a = sum(ord(x) for x in s)
        b = sum(ord(y) for y in t)
        return chr(b-a)
