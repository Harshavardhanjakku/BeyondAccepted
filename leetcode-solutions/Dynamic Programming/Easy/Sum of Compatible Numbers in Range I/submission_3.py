# Problem: Sum of Compatible Numbers in Range I
# Difficulty: Easy
# Topic: Dynamic Programming
# Language: python
# Submission: 3

class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        l = max(0, n - k)
        u = n + k
        tot = 0
        for x in range(l, u + 1):
            if (n & x) == 0:
                tot += x
        return tot
