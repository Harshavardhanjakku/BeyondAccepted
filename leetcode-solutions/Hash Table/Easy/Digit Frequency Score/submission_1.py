# Problem: Digit Frequency Score
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def digitFrequencyScore(self, n):
        tot=0 
        while n :
            tot+=(n%10)
            n//=10
        return tot
