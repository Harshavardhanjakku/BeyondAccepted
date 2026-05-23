# Problem: Divide Two Integers
# Difficulty: Medium
# Topic: Math
# Language: python3
# Submission: 1

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor ==-1:
            return 2147483647
        return int(dividend/divisor)
