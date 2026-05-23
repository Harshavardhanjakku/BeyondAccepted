# GCD of Odd and Even Sums
# Difficulty: Easy
# Language: python3

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int: 
        def gcd(a,b):
            if b%a==0:
                return a
            return gcd(b%a,a)
        return gcd(n*n,n*(n+1))
