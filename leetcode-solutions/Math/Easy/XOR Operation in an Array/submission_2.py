# Problem: XOR Operation in an Array
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

from functools import reduce
import operator

class Solution(object):
    def xorOperation(self, n, start):
        return reduce(operator.xor, (start + 2 * i for i in xrange(n)))

