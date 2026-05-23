# Find the Winner of the Circular Game
# Difficulty: Medium
# Language: python

class Solution(object):
    def findTheWinner(self, n, k):
        mylist = [i + 1 for i in range(n)]
        myptr = 0
        while n > 1:
            myptr = (myptr+ k-1) % n
            n-=1
            mylist.pop(myptr)
        return mylist[0]

