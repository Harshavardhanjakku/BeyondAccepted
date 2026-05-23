# Trim Trailing Vowels
# Difficulty: Easy
# Language: python

class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=len(s)-1
        while i>=0:
            if s[i] not in "aeiou":
                break
            else:
                i-=1
        return s[:i+1]
