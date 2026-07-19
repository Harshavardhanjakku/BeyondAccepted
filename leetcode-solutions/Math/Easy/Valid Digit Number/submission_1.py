# Problem: Valid Digit Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def validDigit(self, n, x):
        s=str(n)
        return str(x) in s and int(s[0])!=x
