# Problem: Minimum Absolute Distance Between Mirror Pairs
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def minMirrorPairDistance(self, nums):
        ans=float('inf')
        dic={}
        for idx,num in enumerate(nums):
            if num in dic:
                ans=min(ans,idx-dic[num])
            temp=num
            rev=0
            while temp>0:
                rev=rev*10+temp%10
                temp//=10
            dic[rev]=idx
        return -1 if ans==float('inf') else ans
