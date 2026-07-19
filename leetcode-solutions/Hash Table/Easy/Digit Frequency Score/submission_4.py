# Problem: Digit Frequency Score
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 4

class Solution(object):
    def digitFrequencyScore(self, n):
        return n - 9 * (
            n // 10 +
            n // 100 +
            n // 1000 +
            n // 10000 +
            n // 100000 +
            n // 1000000 +
            n // 10000000 +
            n // 100000000 +
            n // 1000000000 +
            n // 10000000000 +
            n // 100000000000 +
            n // 1000000000000 +
            n // 10000000000000 +
            n // 100000000000000 +
            n // 1000000000000000 +
            n // 10000000000000000 +
            n // 100000000000000000 +
            n // 1000000000000000000
        )
