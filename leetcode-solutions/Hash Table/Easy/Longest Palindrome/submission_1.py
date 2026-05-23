# Problem: Longest Palindrome
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        for i in s:
            if i not in dic :
                dic[i]=1
            else:
                dic[i]+=1
        tot=0
        flag=False
        for i in dic:
            res=dic[i]
            if res%2==1:
                flag=True
            tot+=(res//2)*2
        return 1+tot if flag else tot
