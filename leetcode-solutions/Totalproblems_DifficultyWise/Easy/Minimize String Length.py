# Minimize String Length
# Difficulty: Easy
# Language: python

class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(set(s))
