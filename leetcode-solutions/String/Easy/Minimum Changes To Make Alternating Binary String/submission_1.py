# Problem: Minimum Changes To Make Alternating Binary String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def minOperations(self,s):
        fc=0
        sc=0
        for i in range(len(s)):
            if s[i]!=str(i%2):
                fc+=1
            if s[i]!=str((i+1)%2):
                sc+=1
        return min(fc,sc)

