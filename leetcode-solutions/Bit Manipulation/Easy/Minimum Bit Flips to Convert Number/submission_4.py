# Problem: Minimum Bit Flips to Convert Number
# Difficulty: Easy
# Topic: Bit Manipulation
# Language: python
# Submission: 4

class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        c=0
        s=bin(start)[2::]
        g=bin(goal)[2::]
        m=len(s)
        n=len(g)
        if m>n:
            g='0'*(m-n)+g
        else:
            s="0"*(n-m)+s
        c=0
        for i in range(max(m,n)):
            if s[i]!=g[i]:
                c+=1
        return c

       


        
