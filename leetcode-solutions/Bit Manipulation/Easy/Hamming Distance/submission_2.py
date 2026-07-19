# Problem: Hamming Distance
# Difficulty: Easy
# Topic: Bit Manipulation
# Language: python
# Submission: 2

class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y
        count = 0
        while xor:
            count += xor & 1
            xor >>= 1
        return count
