# Problem: Assign Cookies
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 6

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        count=0
        i=0
        j=0
        while i<n and j<m:
            if g[i]<=s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j=j+1
        return count       
        
