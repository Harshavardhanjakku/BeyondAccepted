# Unique Binary Search Trees
# Difficulty: Medium
# Language: python

class Solution(object):
    def numTrees(self, n):
        import math
        return math.factorial(2*n) // (math.factorial(n+1) * math.factorial(n))
