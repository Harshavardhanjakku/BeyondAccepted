# Problem: Calculate Money in Leetcode Bank
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def totalMoney(self,n):
        weeks=n//7
        days=n%7
        ans=28*weeks
        ans+=7*weeks*(weeks-1)//2
        ans+=weeks*days
        ans+=days*(days+1)//2
        return ans
