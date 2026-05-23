# Construct the Rectangle
# Difficulty: Easy
# Language: python

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        i=int(area**0.5)
        if i*i==area:
            return [i,i]
        else:
            while (i>0):
                if area%i==0:
                    break
                else:
                    i-=1
            if area//i>i:
                        return [area//i,i]
            else:
                        return [i,area//i]
