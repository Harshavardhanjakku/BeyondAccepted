# Problem: XOR Operation in an Array
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res=start
        for _ in range(1,n):
            res^=start+2*_
        return res
