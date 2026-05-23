# Problem: Reverse Degree of a String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 3

class Solution(object):
    def reverseDegree(self, s):
        return sum((26 - (ord(ch) - ord('a'))) * (i + 1)  for i, ch in enumerate(s))
