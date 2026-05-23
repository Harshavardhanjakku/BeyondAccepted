# Problem: Find the Difference
# Difficulty: Easy
# Topic: Hash Table
# Language: python3
# Submission: 3

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lettersarray=[0]*26
        for i in s:
            ind=ord(i)-97
            lettersarray[ind]+=1
        for i in t:
            ind=ord(i)-97
            lettersarray[ind]-=1
        for i in range(26):
            if lettersarray[i]==-1:
                ind=97+i
                return chr(ind)
