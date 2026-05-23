# Problem: Is Subsequence
# Difficulty: Easy
# Topic: Two Pointers
# Language: python
# Submission: 1

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m=len(s)
        n=len(t)
        i=0
        j=0
        while j<n:
            if i>=m :
                return True
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==m
