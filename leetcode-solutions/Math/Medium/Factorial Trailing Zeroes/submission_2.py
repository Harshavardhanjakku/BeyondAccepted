# Problem: Factorial Trailing Zeroes
# Difficulty: Medium
# Topic: Math
# Language: python3
# Submission: 2

class Solution:
    def trailingZeroes(self, n: int) -> int:
        import math
        res=1
        while(n>0):
            res*=n
            n=n-1
        count=0
        while(res%10==0):
            count+=1
            res//=10
        return count
        

        
