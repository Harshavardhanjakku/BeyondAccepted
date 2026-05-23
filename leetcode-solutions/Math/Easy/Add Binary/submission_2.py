# Problem: Add Binary
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
+        """
        return bin(int(a,2)+int(b,2))[2::]
