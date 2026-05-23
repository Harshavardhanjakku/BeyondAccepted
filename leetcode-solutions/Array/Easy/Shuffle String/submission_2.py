# Problem: Shuffle String
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        newStr=""
        for i in range(len(s)):
            ind=indices.index(i)
            newStr+=s[ind]
        return newStr
