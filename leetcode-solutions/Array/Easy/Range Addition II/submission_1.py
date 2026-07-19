# Problem: Range Addition II
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def maxCount(self,m,n,ops):
        if not ops:
            return m*n
        mina=m
        minb=n
        for a,b in ops:
            mina=min(mina,a)
            minb=min(minb,b)
        return mina*minb
