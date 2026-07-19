# Problem: String to Integer (atoi)
# Difficulty: Medium
# Topic: String
# Language: python
# Submission: 3

class Solution(object):
    def myAtoi(self, s):
        s = s.strip()

        num = 0
        sign = False
        seen = False

        for i in s:

            if i == "-" and not seen:
                sign = True
                seen = True

            elif i == "+" and not seen:
                seen = True

            elif i.isdigit():
                seen = True
                num = num * 10 + int(i)

            else:
                break

        num = -num if sign else num

        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num
