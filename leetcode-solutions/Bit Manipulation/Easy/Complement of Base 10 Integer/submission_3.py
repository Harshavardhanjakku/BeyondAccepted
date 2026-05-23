# Problem: Complement of Base 10 Integer
# Difficulty: Easy
# Topic: Bit Manipulation
# Language: python
# Submission: 3

import math

class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        compliment = ~n
        zerolength = int(math.log(n, 2)) + 1
        tot = ~0
        onemask = 1 << zerolength
        zeromask = onemask - 1
        return compliment & zeromask
