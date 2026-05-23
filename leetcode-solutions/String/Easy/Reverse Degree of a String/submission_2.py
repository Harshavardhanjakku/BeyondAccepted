# Problem: Reverse Degree of a String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def reverseDegree(self, s): 
        z=0
        for i in range(len(s)):
            z+=(123-ord(s[i]))*(i+1)
        return z
