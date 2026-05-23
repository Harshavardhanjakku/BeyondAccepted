# Problem: GCD of Odd and Even Sums
# Difficulty: Easy
# Topic: Math
# Language: python3
# Submission: 1

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int: 
        def gcd(a,b):
            if b%a==0:
                return a
            return gcd(b%a,a)
        return gcd(n*n,n*(n+1))
