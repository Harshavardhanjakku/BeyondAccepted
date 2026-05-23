# Problem: Valid Anagram
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 4

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==len(t):
            if sorted(s)==sorted(t):
                return True
            else:
                return False
        else:
            return False
        
        
