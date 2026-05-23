# First Letter to Appear Twice
# Difficulty: Easy
# Language: python

class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        myset=set()
        for i in s:
            if i in myset:
                return i
            else:
                myset.add(i)
