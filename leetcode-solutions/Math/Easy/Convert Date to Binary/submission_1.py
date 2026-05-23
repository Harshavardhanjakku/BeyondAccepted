# Problem: Convert Date to Binary
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        datelist=date.split("-")
        for i in range(len(datelist)):
            datelist[i]=bin(int(datelist[i]))[2:]
        return "-".join(datelist)
