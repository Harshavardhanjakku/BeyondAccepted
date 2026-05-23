# Number Of Rectangles That Can Form The Largest Square
# Difficulty: Easy
# Language: python

class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        s=[]
        for i in rectangles:
            if i[0]<i[1]:
                s.append(i[0])
            else:
                s.append(i[1])
        return s.count(max(s))
