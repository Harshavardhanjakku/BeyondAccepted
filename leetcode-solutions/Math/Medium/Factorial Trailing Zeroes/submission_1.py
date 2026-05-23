# Problem: Factorial Trailing Zeroes
# Difficulty: Medium
# Topic: Math
# Language: python3
# Submission: 1

class Solution:
    def trailingZeroes(self, n: int) -> int:
        import math
        count=0
        while(n>0):
            n=n//5
            count+=n
        return count
        
        

        
