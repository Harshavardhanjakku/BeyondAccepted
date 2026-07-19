# Problem: Sum of Primes Between Number and Its Reverse
# Difficulty: Medium
# Topic: Math
# Language: python3
# Submission: 2

from bisect import bisect_left,bisect_right 
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        rev=int(str(n)[::-1])
        mn=min(n,rev)
        mx=max(n,rev)
        prime=[True]*(mx+1)
        if mx>=0:
            prime[0]=False
        if mx>=1:
            prime[1]=False
        p=2
        while p*p<=mx:
            if prime[p]:
                for i in range(p*p,mx+1,p):
                    prime[i]=False
            p+=1
        primes=[]
        prefix=[0]
        for i in range(2,mx+1):
            if prime[i]:
                primes.append(i)
                prefix.append(prefix[-1]+i)
        left=bisect_left(primes,mn)
        right=bisect_right(primes,mx)
        return prefix[right]-prefix[left]
