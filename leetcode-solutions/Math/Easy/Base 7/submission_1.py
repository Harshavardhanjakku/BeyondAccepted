# Problem: Base 7
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        flag = num < 0
        num = abs(num)
        res = []
        while num > 0:
            res.append(str(num % 7))
            num //= 7
        ans = "".join(res[::-1])
        return "-" + ans if flag else ans
