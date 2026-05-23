# Problem: Maximum Repeating Substring
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def maxRepeating(self, sequence, word):
        k=0
        while word*(k+1) in sequence:
            k+=1
        return k
