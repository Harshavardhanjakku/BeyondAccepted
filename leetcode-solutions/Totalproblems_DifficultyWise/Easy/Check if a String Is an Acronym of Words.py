# Check if a String Is an Acronym of Words
# Difficulty: Easy
# Language: python

class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        m=""
        for i in words:
            m+=i[0]
        return True if m==s else False

