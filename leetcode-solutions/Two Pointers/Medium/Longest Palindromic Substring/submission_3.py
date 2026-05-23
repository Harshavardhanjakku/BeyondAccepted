# Problem: Longest Palindromic Substring
# Difficulty: Medium
# Topic: Two Pointers
# Language: python
# Submission: 3

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
                temp=s[i:j+1]
                if maxi<(j-i)and temp==temp[::-1]:
                    maxi=j-i
                    mystr=s[i:j+1]
        return mystr

