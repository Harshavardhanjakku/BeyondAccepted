# Problem: GCD of Odd and Even Sums
# Difficulty: Easy
# Topic: Math
# Language: python3
# Submission: 2

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        os=n*n
        es=os+n
        def gcd(a,b):
            if b%a==0:
                return a
            return gcd(b%a,a)
        return gcd(os,es)
