# Problem: Total Waviness of Numbers in Range I
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def totalWaviness(self, num1, num2):
        tot = 0
        for num in range(num1, num2 + 1):
            digits = list(map(int, str(num)))
            for i in range(1, len(digits) - 1):
                if ((digits[i] > digits[i - 1] and digits[i] > digits[i + 1]) or
                    (digits[i] < digits[i - 1] and digits[i] < digits[i + 1])):
                    tot += 1
        return tot
