# Factorial Trailing Zeroes
# Difficulty: Medium
# Language: python3

class Solution:
    def trailingZeroes(self, n: int) -> int:
        import math
        count=0
        while(n>0):
            n=n//5
            count+=n
        return count
        
        

        
