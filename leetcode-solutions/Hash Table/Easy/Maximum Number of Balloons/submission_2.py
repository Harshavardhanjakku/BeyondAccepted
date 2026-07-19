# Problem: Maximum Number of Balloons
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 2

from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        c = Counter(text)
        return min(
            c['b'],
            c['a'],
            c['l'] // 2,
            c['o'] // 2,
            c['n']
        )
