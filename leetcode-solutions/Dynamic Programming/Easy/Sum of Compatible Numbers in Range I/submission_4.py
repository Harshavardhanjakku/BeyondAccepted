# Problem: Sum of Compatible Numbers in Range I
# Difficulty: Easy
# Topic: Dynamic Programming
# Language: python
# Submission: 4

class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        lowerlimit = max(0, n - k)
        upperlimit = n + k
        tot = 0
        for x in range(lowerlimit, upperlimit + 1):
            if (n & x) == 0:
                tot += x
        return tot
