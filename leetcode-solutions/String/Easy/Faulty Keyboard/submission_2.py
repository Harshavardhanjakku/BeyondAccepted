# Problem: Faulty Keyboard
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns=""
        for x in s:
            if x!="i":
                ns+=x
            else:
                ns=ns[::-1]
        return ns

