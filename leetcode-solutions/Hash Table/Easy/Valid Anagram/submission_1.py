# Problem: Valid Anagram
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        letters=[0]*26
        for i in range(len(s)):
            letters[ord(s[i])-97]+=1
            letters[ord(t[i])-97]-=1
        return letters==[0]*26
