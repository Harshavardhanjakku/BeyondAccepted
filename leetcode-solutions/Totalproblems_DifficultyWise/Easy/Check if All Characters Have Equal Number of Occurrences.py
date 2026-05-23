# Check if All Characters Have Equal Number of Occurrences
# Difficulty: Easy
# Language: python

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={}
        myset=set(s)
        for i in myset:
            dic[i]=s.count(i)
        if len(set(dic.values()))==1:
            return True
        else:
            return False

