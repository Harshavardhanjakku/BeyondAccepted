# Problem: Minimum Changes To Make Alternating Binary String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 3

class Solution(object):
    def minOperations(self,s):
        n=len(s)
        curr1=int(s[0])
        curr2=int(not int(s[0]))
        fcount=0
        bcount=1
        for i in range(1,n):
            if int(s[i])==int(not curr1):
                curr1=int(s[i])
            else:
                curr1=int(not curr1)
                fcount+=1
            if int(s[i])==int(not curr2):
                curr2=int(s[i])
            else:
                curr2=int(not curr2)
                bcount+=1
        return min(fcount,bcount)
