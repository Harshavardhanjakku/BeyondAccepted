# Minimum Sum of Four Digit Number After Splitting Digits
# Difficulty: Easy
# Language: python

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        mylist=list(map(int,str(num)))
        mylist.sort()
        new1=mylist[0]*10+mylist[2]
        new2=mylist[1]*10+mylist[3]
        return new1+new2
