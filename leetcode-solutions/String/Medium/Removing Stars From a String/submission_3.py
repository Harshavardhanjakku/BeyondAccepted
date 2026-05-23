# Problem: Removing Stars From a String
# Difficulty: Medium
# Topic: String
# Language: python
# Submission: 3

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns=""
        for i in range(len(s)):
            if s[i]=="*":
                ns=ns[:-1]
            else:
                ns+=s[i]
        return ns

