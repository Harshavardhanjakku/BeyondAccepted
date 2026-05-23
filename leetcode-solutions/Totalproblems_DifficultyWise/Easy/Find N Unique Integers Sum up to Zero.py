# Find N Unique Integers Sum up to Zero
# Difficulty: Easy
# Language: python3

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ n * (1 - n) >> 1] + list(range(1, n))
        
