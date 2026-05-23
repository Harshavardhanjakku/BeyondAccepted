# Problem: Isomorphic Strings
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def isIsomorphic(self, s, t):
        m=len(s)
        n=len(t)
        if m!=n:
            return False
        dic={}
        used=set()
        for idx in range(n):
            sc=s[idx]
            tc=t[idx]
            if sc not in dic:
                if tc in used:
                    return False
                dic[sc]=tc
                used.add(tc)
            else:
                if dic[sc]!=tc:
                    return False    
        return True
