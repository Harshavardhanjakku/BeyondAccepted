# First Unique Character in a String
# Difficulty: Easy
# Language: python

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        myset=set(s)
        l=[]
        for i in myset:
            if s.count(i)==1:
                l.append(s.index(i))
        return -1 if len(l)==0 else min(l)
