# Problem: Factorial Trailing Zeroes
# Difficulty: Medium
# Topic: Math
# Language: python3
# Submission: 3

class Solution:
    def trailingZeroes(self, n: int) -> int:
        import math
        res=math.factorial(n)
        count=0
        while(res%10==0):
            count+=1
            res//=10
        return count
        

        
