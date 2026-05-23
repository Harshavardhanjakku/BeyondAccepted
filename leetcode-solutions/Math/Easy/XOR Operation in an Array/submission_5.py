# Problem: XOR Operation in an Array
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 5

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res=start
        i=1
        while i<n:
            res=res^(start+2*i)
            i+=1
        return res
