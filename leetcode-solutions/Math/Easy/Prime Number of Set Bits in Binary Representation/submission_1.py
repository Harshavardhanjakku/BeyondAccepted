# Problem: Prime Number of Set Bits in Binary Representation
# Difficulty: Easy
# Topic: Math
# Language: python3
# Submission: 1

class Solution:
    def countPrimeSetBits(self,left:int,right:int)->int:
        def checkprime(n):
            if n<2:
                return False
            if n==2:
                return True
            if n%2==0:
                return False
            for i in range(3,int(n**0.5)+1,2):
                if n%i==0:
                    return False
            return True
        def countsetbits(n):
            count=0
            while n:
                n=n&(n-1)
                count+=1
            return count
        tot=0
        for num in range(left,right+1):
            if checkprime(countsetbits(num)):
                tot+=1
        return tot
