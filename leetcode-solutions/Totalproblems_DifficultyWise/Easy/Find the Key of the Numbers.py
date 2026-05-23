# Find the Key of the Numbers
# Difficulty: Easy
# Language: python

class Solution(object):
    def generateKey(self, num1, num2, num3):
        n1 = str(num1).zfill(4)
        n2 = str(num2).zfill(4)
        n3 = str(num3).zfill(4)

        res = ""
        for i in range(4):
            res += min(n1[i], n2[i], n3[i])

        return int(res)

