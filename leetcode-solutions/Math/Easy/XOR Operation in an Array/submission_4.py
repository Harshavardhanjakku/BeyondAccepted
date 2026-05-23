# Problem: XOR Operation in an Array
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 4

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res=start
        for i in range(1,n):
            res^=start+2*i
        return res
