# Problem: Find All Anagrams in a String
# Difficulty: Medium
# Topic: Hash Table
# Language: python3
# Submission: 1

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        pdic={}
        for ch in p:
            pdic[ch]=pdic.get(ch,0)+1
        d={}
        for ch in s[:k]:
            d[ch]=d.get(ch,0)+1
        res=[]
        start=0
        if d==pdic:
            res.append(start)
        for end in range(k,len(s)):
            d[s[start]]-=1
            if d[s[start]]==0:
                del d[s[start]]
            d[s[end]]=d.get(s[end],0)+1
            start+=1
            if d==pdic:
                res.append(start)
        return res
