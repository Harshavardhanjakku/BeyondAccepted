# Problem: Sum of Elements With Frequency Divisible by K
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 3

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        tot=0
        for key,value in dic.items() :
            if value%k==0:
                tot+=key*value
        return tot
