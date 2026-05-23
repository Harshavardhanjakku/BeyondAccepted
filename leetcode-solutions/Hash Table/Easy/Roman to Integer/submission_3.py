# Problem: Roman to Integer
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 3

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        level=1
        leveldic={}
        for x in "IVXLCDM" :
            leveldic[x]=level
            level+=1
        valuedic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n=len(s)
        total=0
        for i in range(n-1):
            char=s[i]
            nextchar=s[i+1]
            if leveldic[char]<leveldic[nextchar]:
                total-=valuedic[char]
            else:
                total+=valuedic[char]
        return total+valuedic[s[-1]]

