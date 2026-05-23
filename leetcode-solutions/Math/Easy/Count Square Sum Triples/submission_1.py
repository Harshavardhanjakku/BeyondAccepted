# Problem: Count Square Sum Triples
# Difficulty: Easy
# Topic: Math
# Language: python3
# Submission: 1

class Solution:
    def countTriples(self, n: int) -> int:
        import math
        count = 0
        
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                c2 = a*a + b*b
                c = math.isqrt(c2)
                if c <= n and c*c == c2:
                    count += 2   
        
        return count

