# Problem: Integer Break
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def integerBreak(self, n):
        if n <= 3:
            return n - 1
        tot = n // 3
        rem = n % 3
        if rem == 0:
            return 3 ** tot
        elif rem == 1:
            return 4 * (3 ** (tot - 1))
        else:
            return 2 * (3 ** tot)
