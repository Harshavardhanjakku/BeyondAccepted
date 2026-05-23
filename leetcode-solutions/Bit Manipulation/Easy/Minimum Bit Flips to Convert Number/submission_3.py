# Problem: Minimum Bit Flips to Convert Number
# Difficulty: Easy
# Topic: Bit Manipulation
# Language: python
# Submission: 3

class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        res=start^goal
        c=0
        while res:
            res=res&(res-1)
            c+=1
        return c 
