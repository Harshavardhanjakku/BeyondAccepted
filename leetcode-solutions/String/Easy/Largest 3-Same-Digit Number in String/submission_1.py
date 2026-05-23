# Problem: Largest 3-Same-Digit Number in String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(9,-1,-1):
            lno=str(i)*3
            if lno in num:
                return lno
        return ""
