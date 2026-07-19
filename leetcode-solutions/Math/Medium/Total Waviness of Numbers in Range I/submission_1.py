# Problem: Total Waviness of Numbers in Range I
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def totalWaviness(self, a, b):
        res = 0
        for n in range(a, b + 1):
            temp = n
            while temp >= 100:
                r = temp % 10
                c = (temp // 10) % 10
                l = (temp // 100) % 10
                if (c > l and c > r) or (c < l and c < r):
                    res += 1
                temp //= 10
        return res
