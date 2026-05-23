# Problem: Minimum Absolute Distance Between Mirror Pairs
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def minMirrorPairDistance(self, nums):
        minDist=float('inf')
        mp={}
        for i,n in enumerate(nums):
            if n in mp:
                minDist=min(minDist,i-mp[n])
            rev=0
            temp=n
            while temp>0:
                rev=rev*10+temp%10
                temp//=10
            mp[rev]=i
        return -1 if minDist==float('inf') else minDist
