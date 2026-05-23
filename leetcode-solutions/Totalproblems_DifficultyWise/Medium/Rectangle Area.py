# Rectangle Area
# Difficulty: Medium
# Language: python

class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        def area(x1,y1,x2,y2):
            length=x2-x1
            breadth=y2-y1
            return length*breadth
        fra=area(ax1,ay1,ax2,ay2)
        sra=area(bx1,by1,bx2,by2)
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        bottom = max(ay1, by1)
        top = min(ay2, by2)
        ow = max(0, right - left)
        oh= max(0, top - bottom)
        common=ow*oh
        return fra+sra-common
        
