# Problem: Minimum Changes To Make Alternating Binary String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def minOperations(self,s):
        n=len(s)
        fcount=0
        bcount=0
        for i in range(n):
            if int(s[i])!=i%2:
                fcount+=1
            if int(s[i])!=(i+1)%2:
                bcount+=1
        return min(fcount,bcount)
