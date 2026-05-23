# Problem: Divide Two Integers
# Difficulty: Medium
# Topic: Math
# Language: python3
# Submission: 3

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==(2**31):
            return dividend-1
        elif dividend == -2147483648 and divisor ==-1:
            return 2147483647
        return int(dividend/divisor)
