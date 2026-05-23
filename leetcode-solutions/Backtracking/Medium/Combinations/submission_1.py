# Problem: Combinations
# Difficulty: Medium
# Topic: Backtracking
# Language: python
# Submission: 1

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations

        return list(combinations([x for x in range(1, n + 1)], k))

