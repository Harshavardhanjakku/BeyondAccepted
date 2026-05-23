# Add Binary
# Difficulty: Easy
# Language: python

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        """
        carry = 0
        result = []
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(max(len(a), len(b)))
        for i in range(len(a) - 1, -1, -1):
            res = int(a[i])+int(b[i])+ carry
            result.append(str(res % 2))
            carry = res // 2
        if carry:
            result.append("1")
        result.reverse()
        return "".join(result)

