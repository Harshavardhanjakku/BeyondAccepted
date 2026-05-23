# Problem: Maximum Product of Word Lengths
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic={}
        for i in words :
            dic[i]=set(i)
        n=len(words)
        maxi=0
        for i in range(n-1):
            for j in range(i+1,n):
                if dic[words[i]]&dic[words[j]]==set():
                    maxi=max(maxi,len(words[i])*len(words[j]))
        return maxi

