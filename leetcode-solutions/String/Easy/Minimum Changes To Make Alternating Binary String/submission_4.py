# Problem: Minimum Changes To Make Alternating Binary String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 4

class Solution(object):
    def minOperations(self,s):
        n=len(s)
        curr=int(s[0])
        fcount=0
        for i in range(1,n):
            if int(s[i])==int(not curr):
                curr=int(s[i])
            else:
                curr=int(not curr)
                fcount+=1
        curr=int(not int(s[0]))
        bcount=1
        for i in range(1,n):
            if int(s[i])==int(not curr):
                curr=int(s[i])
            else:
                curr=int(not curr)
                bcount+=1
        return min(fcount,bcount)
