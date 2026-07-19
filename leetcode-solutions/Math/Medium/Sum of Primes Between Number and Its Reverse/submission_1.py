# Problem: Sum of Primes Between Number and Its Reverse
# Difficulty: Medium
# Topic: Math
# Language: python3
# Submission: 1

MAXX = 10**5
prime = list(range(MAXX))
prime[0] = prime[1] = 0
for i in range(MAXX):
    if prime[i]:
        for j in range(i * 2, MAXX, i):
            prime[j] = 0
for i in range(1, MAXX):
    prime[i] += prime[i - 1]
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        l, r = min(n, r), max(n, r)
        return prime[r] - (prime[l - 1] if l != 0 else 0)
        
        
