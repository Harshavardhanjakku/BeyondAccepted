# Find First Palindromic String in the Array
# Difficulty: Easy
# Language: python

class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            if i==i[::-1]:
                return i
                break
        return ""
