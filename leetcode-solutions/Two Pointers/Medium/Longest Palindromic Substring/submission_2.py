# Problem: Longest Palindromic Substring
# Difficulty: Medium
# Topic: Two Pointers
# Language: python
# Submission: 2

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxi=0
        n=len(s)
        mystr=s[0]
        for i in range(n):
            for j in range(i+1,n):
                if maxi<(j-i)and s[i:j+1]==s[i:j+1][::-1]:
                    maxi=j-i
                    mystr=s[i:j+1]
        return mystr

