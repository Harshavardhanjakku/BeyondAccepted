# Problem: Minimum Bit Flips to Convert Number
# Difficulty: Easy
# Topic: Bit Manipulation
# Language: python
# Submission: 2

class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        k=start^goal
        c=0
        while k:
            if k&1:
                c+=1
            k>>=1
        return c
            
