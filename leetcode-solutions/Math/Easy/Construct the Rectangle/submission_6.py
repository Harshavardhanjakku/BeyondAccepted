# Problem: Construct the Rectangle
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 6

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
            while (i<=area):
                if area%i==0:
                    if area//i<i:
                        return [i,area//i]
                    else:
                        return [area//i,i]
                else:
                    i+=1
