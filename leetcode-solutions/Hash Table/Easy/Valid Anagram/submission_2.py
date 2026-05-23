# Problem: Valid Anagram
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 2

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m=len(s)
        n=len(t)
        if m!=n:
            return False
        letters=[0]*26
        for i in s :
            letters[ord(i)-97]+=1
        for i in t:
            letters[ord(i)-97]-=1
        for i in range(26):
            if letters[i]!=0:
                return False
        return True
