# Problem: Find Closest Person
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def findClosest(self, x, y, z):
        d1 = abs(x - z)
        d2 = abs(y - z)

        if d1 < d2:
            return 1
        elif d2 < d1:
            return 2
        else:
            return 0
