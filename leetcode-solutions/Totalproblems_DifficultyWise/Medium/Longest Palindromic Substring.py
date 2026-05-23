# Longest Palindromic Substring
# Difficulty: Medium
# Language: python

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s :
            return 0 
        n=len(s)
        count=0
        start=0
        end=0
        for i in range(n):
            left,right=i,i
            while (left>=0 and right<n and s[left]==s[right]):
                if (right-left+1 > count):
                    count=right-left+1
                    start=left
                    end=right
                left-=1
                right+=1
            left,right=i,i+1
            while (left>=0 and right<n and s[left]==s[right]):
                if (right-left+1 > count):
                    count=right-left+1
                    start=left
                    end=right
                left-=1
                right+=1
        return s[start:end+1]
