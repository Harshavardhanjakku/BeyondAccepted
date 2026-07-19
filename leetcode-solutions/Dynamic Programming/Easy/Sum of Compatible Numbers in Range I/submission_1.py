# Problem: Sum of Compatible Numbers in Range I
# Difficulty: Easy
# Topic: Dynamic Programming
# Language: python
# Submission: 1

class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        ans = 0
        for x in range(max(1, n - k), n + k + 1):
            if (n & x) == 0:
                ans += x
        return ans
