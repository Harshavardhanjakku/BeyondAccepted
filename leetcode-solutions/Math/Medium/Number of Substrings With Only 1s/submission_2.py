# Problem: Number of Substrings With Only 1s
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def numSub(self,s):
        start=0
        n=len(s)
        count=0
        while start<n:
            if s[start]=="0":
                start+=1
            else:
                end=start
                while end<n and s[end]=="1":
                    end+=1
                l=end-start
                count+=l*(l+1)//2
                start=end
        return count%(10**9+7)
