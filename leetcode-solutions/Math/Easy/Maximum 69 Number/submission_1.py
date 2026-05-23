# Problem: Maximum 69 Number
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        l=list(map(str,str(num)))
        ind=0
        for i in l:
            if i=="6":
                l[ind]="9"
                break
            ind+=1
        return int("".join(l))


