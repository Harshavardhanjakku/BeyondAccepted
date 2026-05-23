# Problem: Cells in a Range on an Excel Sheet
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        firstval=ord(s[0])
        findx=int(s[1])
        secondval=ord(s[3])
        sindx=int(s[-1])
        return [chr(i)+str(j) for i in range(firstval,secondval+1) for j in range(findx,sindx+1)]

