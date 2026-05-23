# Pass the Pillow
# Difficulty: Easy
# Language: python

class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        l=[x for x in range(1,n+1)]
        rl=[x for x in range(n-1,1,-1)]
        l.extend(rl)
        if time<len(l):
            return l[time]
        else:
            r=time%len(l)
            return l[r]
