# Problem: Faulty Keyboard
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns=""
        for x in s:
            if x=="i":
                ns=ns[::-1]
            else:
                ns+=x  
        return ns

