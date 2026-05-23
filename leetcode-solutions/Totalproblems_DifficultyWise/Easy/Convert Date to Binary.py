# Convert Date to Binary
# Difficulty: Easy
# Language: python

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
