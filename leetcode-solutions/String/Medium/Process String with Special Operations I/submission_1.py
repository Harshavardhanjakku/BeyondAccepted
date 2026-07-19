# Problem: Process String with Special Operations I
# Difficulty: Medium
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        for i in s :
            if i.islower():
                l.append(i)
            elif l and i=="*":
                l.pop()
            elif i=="#":
                l.extend(l)
            elif i=="%":
                l.reverse()
        return "".join(l)
