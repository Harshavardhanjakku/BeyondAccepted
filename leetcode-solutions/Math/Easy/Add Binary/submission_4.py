# Problem: Add Binary
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 4

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        p,q=a,b
        p,q=int(p,2),int(q,2)
        return bin(p+q)[2::]
