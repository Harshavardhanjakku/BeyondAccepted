# Problem: Permutation Sequence
# Difficulty: Hard
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from itertools import permutations
        return "".join(list(map(str,list(permutations([x for x in range(1,n+1)]))[k-1])))
