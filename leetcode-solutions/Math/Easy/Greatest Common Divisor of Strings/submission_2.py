# Problem: Greatest Common Divisor of Strings
# Difficulty: Easy
# Topic: Math
# Language: python3
# Submission: 2

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        m = len(str1)
        n = len(str2)
 
        cmpstr = str1 if m <= n else str2

        temp = ""
        maxi = 0
        L = len(cmpstr)
        for i in range(L):
            for j in range(i + 1, L + 1):
                sub = cmpstr[i:j]
                if len(sub) <= maxi:
                    continue 
                if str1.replace(sub, "") == "" and str2.replace(sub, "") == "":
                    temp = sub
                    maxi = len(sub)
        return temp

