# Number of Substrings With Only 1s
# Difficulty: Medium
# Language: python

class Solution(object):
    def numSub(self,s):
        t=0
        MOD=1000000007
        for i in s.split("0"):
            n=len(i)
            t+=n*(n+1)//2
        return t%(MOD)
