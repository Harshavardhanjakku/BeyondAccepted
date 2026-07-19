# Problem: Split a String in Balanced Strings
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot=0
        rc=0
        lc=0
        for i in s:
            if i=="R":
                rc+=1
            else:
                lc+=1
            if lc==rc:
                tot+=1
                lc=0
                rc=0
        return tot

