# Problem: Find the Difference
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 2

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        for i in t:
            dic[i]=dic.get(i,0)-1
        for i in dic:
            if dic[i]==-1:
                return i
