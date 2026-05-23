# Faulty Keyboard
# Difficulty: Easy
# Language: python

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

