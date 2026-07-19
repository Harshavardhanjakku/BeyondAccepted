# Problem: Digit Frequency Score
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 3

class Solution(object):
    def digitFrequencyScore(self, n):
        ans = n
        p = 10
        while p <= n:
            ans -= 9 * (n // p)
            p *= 10
        return ans
